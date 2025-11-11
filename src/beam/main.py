import random
import os
import re
import time
import math
import pickle
from collections import defaultdict
from typing import List, Dict
import json
import tiktoken
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
from json_repair import repair_json
import concurrent.futures
import threading
import cProfile
import pstats
import asyncio
import ast
import multiprocessing
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.memory import ConversationSummaryBufferMemory
from langchain.schema import BaseMessage, HumanMessage, AIMessage
from langchain.memory import ConversationBufferWindowMemory
from concurrent.futures import ProcessPoolExecutor

from src.llm import *
from src.prompts import *
from src.beam.profile_creation import create_profile
from src.beam.utils import extract_time_anchor, get_token_number


class ConversationSummaryBuffer:
    def __init__(self, llm, max_tokens=8000, recent_messages_count=6, max_summary_tokens=2000):
        self.llm = llm
        self.max_tokens = max_tokens
        self.recent_messages_count = recent_messages_count
        self.max_summary_tokens = max_summary_tokens
        self.messages = []
        self.summary = ""

        self.token_encoder = self._get_token_encoder()

    def _get_token_encoder(self):
        """Initialize the best available token encoder"""
        try:
            encoders_to_try = ["cl100k_base", "p50k_base", "r50k_base"]

            for encoding_name in encoders_to_try:
                try:
                    encoder = tiktoken.get_encoding(encoding_name)
                    print(f"Using tiktoken with {encoding_name} encoding")
                    return encoder
                except:
                    continue
        except:
            pass

    def estimate_tokens(self, text):
        """Count tokens using the initialized encoder"""
        if not text:
            return 0

        text = str(text)

        if self.token_encoder:
            try:
                return len(self.token_encoder.encode(text))
            except:
                return len(text) // 3
        else:
            return len(text) // 3

    def get_total_tokens(self):
        """Calculate total tokens in current messages + summary"""
        message_tokens = sum(self.estimate_tokens(
            msg["content"]) for msg in self.messages)
        summary_tokens = self.estimate_tokens(
            self.summary) if self.summary else 0
        return message_tokens + summary_tokens

    def add_message(self, role, content):
        """Add a new message and trigger compression if needed"""
        self.messages.append({"role": role, "content": content})

        self._ensure_token_limit()

    def save_context(self, user_input, ai_output):
        """Add user-AI exchange"""
        self.add_message("user", user_input)
        self.add_message("assistant", ai_output)

    def _ensure_token_limit(self):
        """Ensure total tokens stay within limit through multiple strategies"""
        max_iterations = 10
        iteration = 0

        while self.get_total_tokens() > self.max_tokens and iteration < max_iterations:
            iteration += 1

            # Strategy 1: Normal compression (if we have enough messages)
            if self.messages:
                self._compress_messages()
                continue

            # Strategy 2: Reduce recent message count if normal compression isn't enough
            if self.messages:  # Keep at least 2 messages
                self._reduce_recent_messages()
                continue

            # Strategy 3: Truncate individual messages if still too many tokens
            if self.messages:
                self._truncate_long_messages()
                continue

            # Strategy 4: Compress summary further if it's too large
            if self.summary:
                self._compress_summary_further()
                continue

            break

        if iteration >= max_iterations:
            print(
                f"Warning: Could not reduce tokens below limit after {max_iterations} attempts")

    def _compress_messages(self):
        """Compress messages based on token budget, not fixed count"""
        if not self.messages:
            return

        available_tokens = self.max_tokens - self.max_summary_tokens - 400

        cumulative_tokens = 0
        messages_to_keep = []
        messages_to_summarize = []

        for msg in reversed(self.messages):
            msg_tokens = self.estimate_tokens(msg["content"])

            if cumulative_tokens + msg_tokens <= available_tokens and len(messages_to_keep) < self.recent_messages_count:
                messages_to_keep.insert(0, msg)
                cumulative_tokens += msg_tokens
            else:
                messages_to_summarize.insert(0, msg)

        if messages_to_summarize:
            new_summary = self._create_summary(messages_to_summarize)

            if self.summary:
                combined_text = f"{self.summary}\n\nAdditional context: {new_summary}"
                if self.estimate_tokens(combined_text) > self.max_summary_tokens:
                    self.summary = self._create_meta_summary(
                        self.summary, new_summary)
                else:
                    self.summary = combined_text
            else:
                self.summary = new_summary

            if self.estimate_tokens(self.summary) > self.max_summary_tokens:
                self.summary = self._truncate_summary(self.summary)

            print(f"Compressed {len(messages_to_summarize)} messages into summary. "
                  f"Keeping {len(messages_to_keep)} recent messages.")

        self.messages = messages_to_keep

    def _reduce_recent_messages(self):
        """Reduce messages using pure token-aware selection"""
        if not self.messages:
            return

        summary_tokens = self.estimate_tokens(
            self.summary) if self.summary else 0
        available_tokens = self.max_tokens - summary_tokens - 400

        cumulative_tokens = 0
        messages_to_keep = []
        messages_to_summarize = []

        for msg in reversed(self.messages):
            msg_tokens = self.estimate_tokens(msg["content"])

            if cumulative_tokens + msg_tokens <= available_tokens and len(messages_to_keep) < self.recent_messages_count:
                messages_to_keep.insert(0, msg)
                cumulative_tokens += msg_tokens
            else:
                messages_to_summarize.insert(0, msg)

        if not messages_to_keep and self.messages:
            most_recent = self.messages[-1].copy()
            max_chars = available_tokens * 3

            if len(most_recent["content"]) > max_chars:
                most_recent["content"] = most_recent["content"][:max_chars -
                                                                20] + "... [truncated]"

            messages_to_keep = [most_recent]
            messages_to_summarize = self.messages[:-1]

            print(
                f"Truncated most recent message to fit within {available_tokens} token budget")

        if messages_to_summarize:
            new_summary = self._create_summary(messages_to_summarize)

            if self.summary:
                combined_text = f"{self.summary}\n\nAdditional context: {new_summary}"
                if self.estimate_tokens(combined_text) > self.max_summary_tokens:
                    self.summary = self._create_meta_summary(
                        self.summary, new_summary)
                else:
                    self.summary = combined_text
            else:
                self.summary = new_summary

            if self.estimate_tokens(self.summary) > self.max_summary_tokens:
                self.summary = self._truncate_summary(self.summary)

            self.messages = messages_to_keep

            removed_tokens = sum(self.estimate_tokens(
                msg["content"]) for msg in messages_to_summarize)
            kept_tokens = sum(self.estimate_tokens(
                msg["content"]) for msg in messages_to_keep)

            print(f"Reduced messages: moved {len(messages_to_summarize)} messages ({removed_tokens} tokens) to summary, "
                  f"keeping {len(messages_to_keep)} messages ({kept_tokens} tokens)")

    def _truncate_long_messages(self):
        """Truncate individual messages that are too long"""
        max_message_tokens = (
            self.max_tokens - self.max_summary_tokens) // max(len(self.messages), 1)

        for i, msg in enumerate(self.messages):
            msg_tokens = self.estimate_tokens(msg["content"])
            if msg_tokens > max_message_tokens:
                char_limit = max_message_tokens * 3
                if len(msg["content"]) > char_limit:
                    truncated_content = msg["content"][:char_limit -
                                                       50] + "... [truncated]"
                    self.messages[i]["content"] = truncated_content
                    print(
                        f"Truncated message {i} from {msg_tokens} to ~{max_message_tokens} tokens")

    def _compress_summary_further(self):
        """Compress the summary to be smaller"""
        if not self.summary:
            return

        target_tokens = self.max_summary_tokens // 2

        prompt = f"""Compress this summary to NO MORE than {target_tokens * 3} characters while keeping the most important information:
        {self.summary}
        Compressed summary (under {target_tokens * 3} characters):"""

        try:
            response = self.llm.invoke(prompt)
            if hasattr(response, 'content'):
                compressed = response.content.strip()
            else:
                compressed = str(response).strip()

            if self.estimate_tokens(compressed) < self.estimate_tokens(self.summary):
                self.summary = compressed
                print(
                    f"Compressed summary further to {self.estimate_tokens(compressed)} tokens")
            else:
                self.summary = self._truncate_summary(
                    self.summary, target_tokens)
        except:
            self.summary = self._truncate_summary(self.summary, target_tokens)

    def _create_summary(self, messages):
        """Create summary of messages using LLM with size constraint"""
        if not messages:
            return ""

        conversation_text = ""
        for msg in messages:
            role = "User" if msg["role"] == "user" else "Assistant"
            conversation_text += f"{role}: {msg['content']}\n\n"

        max_chars = self.max_summary_tokens * 3
        summary_prompt = f"""Summarize the following conversation in NO MORE than {max_chars} characters. Focus on key decisions, important information, and progress made. Be concise but preserve important context:
        {conversation_text}
        Summary (keep under {max_chars} characters):"""

        try:
            summary_response = self.llm.invoke(summary_prompt)
            if hasattr(summary_response, 'content'):
                summary = summary_response.content.strip()
            else:
                summary = str(summary_response).strip()

            if self.estimate_tokens(summary) > self.max_summary_tokens:
                summary = self._truncate_summary(summary)

            return summary
        except Exception as e:
            print(f"Error creating summary: {e}")
            fallback = f"Previous conversation covered {len(messages)} exchanges."
            return self._truncate_summary(fallback)

    def _create_meta_summary(self, old_summary, new_summary):
        """Re-summarize when combined summary would be too long"""
        max_chars = self.max_summary_tokens * 3
        meta_prompt = f"""Combine these two summaries into one concise summary of NO MORE than {max_chars} characters:
        Previous Summary: {old_summary}
        Recent Summary: {new_summary}
        Combined Summary (under {max_chars} characters):"""

        try:
            response = self.llm.invoke(meta_prompt)
            if hasattr(response, 'content'):
                meta_summary = response.content.strip()
            else:
                meta_summary = str(response).strip()

            if self.estimate_tokens(meta_summary) > self.max_summary_tokens:
                meta_summary = self._truncate_summary(meta_summary)

            return meta_summary
        except Exception as e:
            print(f"Error creating meta summary: {e}")
            return self._truncate_summary(new_summary)

    def _truncate_summary(self, summary, max_tokens=None):
        """Truncate summary to fit within token limit"""
        target_tokens = max_tokens or self.max_summary_tokens

        if self.estimate_tokens(summary) <= target_tokens:
            return summary

        char_limit = target_tokens * 3
        if len(summary) > char_limit:
            truncated = summary[:char_limit-3] + "..."
            return truncated

        return summary

    def get_messages_for_llm(self, system_prompt=None):
        """Get messages formatted for LLM with summary context"""
        formatted_messages = []

        if system_prompt:
            formatted_messages.append(
                {"role": "system", "content": system_prompt})

        if self.summary:
            summary_content = f"Previous conversation summary: {self.summary}"
            formatted_messages.append(
                {"role": "system", "content": summary_content})

        formatted_messages.extend(self.messages)
        return formatted_messages

    def get_conversation_history_text(self):
        """Get formatted conversation history for templates"""
        if not self.messages:
            return ""

        history_text = ""
        if self.summary:
            history_text += f"Previous Context: {self.summary}\n\n"

        history_text += "Recent Conversations:\n"
        for msg in self.messages:
            role = "User" if msg["role"] == "user" else "Assistant"
            history_text += f"{role}: {msg['content']}\n\n"

        return history_text.strip()

    def clear(self):
        """Clear all messages and summary"""
        self.messages = []
        self.summary = ""

    def get_summary_stats(self):
        """Get statistics about current memory state"""
        return {
            "total_messages": len(self.messages),
            "summary_tokens": self.estimate_tokens(self.summary) if self.summary else 0,
            "message_tokens": sum(self.estimate_tokens(msg["content"]) for msg in self.messages),
            "total_tokens": self.get_total_tokens(),
            "summary_length": len(self.summary),
            "has_summary": bool(self.summary),
            "within_limit": self.get_total_tokens() <= self.max_tokens
        }


def prepare_prompt_within_budget(template, 
                                 replacements, 
                                 memory_obj, 
                                 max_tokens=16000):
    """
    Prepare a prompt while respecting token limits

    Args:
        template: The prompt template with placeholders
        replacements: Dict of key->value replacements
        memory_obj: The ConversationSummaryBuffer instance (for token estimation)
        max_tokens: Maximum allowed tokens
    """
    # Start with the template
    prompt = template

    # Track tokens as we build
    token_count = memory_obj.estimate_tokens(prompt)

    # Sort replacements by priority (most important first)
    priority_order = [
        "current_batch_messages",  # Most recent/relevant
        "ai_last_message",         # Latest response
        "current_plan",            # Current context
        "topic",                   # Core info
        "theme",                   # Core info
        "previous_plans_summary",  # Can be truncated
        "previous_batches"         # Can be truncated most
    ]

    for key in priority_order:
        if f"<{key}>" in prompt and key in replacements:
            value = replacements[key]
            value_tokens = memory_obj.estimate_tokens(value)

            # Check if adding this would exceed budget
            if token_count + value_tokens > max_tokens - 1000:  # Leave buffer
                # Handle based on priority
                if key in ["previous_batches", "previous_plans_summary"]:
                    # These can be truncated
                    available_tokens = max_tokens - token_count - 1000
                    if available_tokens > 100:
                        value = truncate_to_tokens(
                            value, available_tokens, memory_obj)
                    else:
                        value = "[Content omitted due to length]"

                elif key == "current_plan":
                    # Try to truncate but keep essential parts
                    available_tokens = max_tokens - token_count - 1000
                    if available_tokens > 500:
                        value = truncate_to_tokens(
                            value, available_tokens, memory_obj)
                    else:
                        # Extract just the key points
                        value = f"[Plan summary: {value[:200]}...]"

                elif key == "ai_last_message":
                    # Truncate but keep beginning and end
                    available_tokens = max_tokens - token_count - 1000
                    if available_tokens > 300:
                        value = truncate_smart(
                            value, available_tokens, memory_obj)
                    else:
                        value = f"{value[:100]}... [truncated] ...{value[-100:]}"

                elif key in ["topic", "theme"]:
                    # These are usually short, but if not, truncate
                    if value_tokens > 200:
                        value = value[:200] + "..."

                elif key == "current_batch_messages":
                    # This is critical - if it's from memory's conversation history,
                    # we might have access to the summary
                    available_tokens = max_tokens - token_count - 1000
                    if available_tokens > 1000:
                        value = "...[earlier messages truncated]...\n" + \
                            value[-(available_tokens*3):]
                    else:
                        value = "[Messages too long - see summary]"

            prompt = prompt.replace(f"<{key}>", value)
            token_count = memory_obj.estimate_tokens(prompt)

    # Final check
    if token_count > max_tokens:
        print(
            f"Warning: Final prompt still exceeds limit ({token_count} > {max_tokens})")

    return prompt


def truncate_to_tokens(text, 
                       max_tokens, 
                       memory_obj):
    """Truncate text to approximately max_tokens"""
    # Use the memory object's token estimation
    current_tokens = memory_obj.estimate_tokens(text)

    if current_tokens <= max_tokens:
        return text

    # Binary search for the right length
    left, right = 0, len(text)
    result = text

    while left < right:
        mid = (left + right + 1) // 2
        truncated = text[:mid] + "... [truncated]"
        tokens = memory_obj.estimate_tokens(truncated)

        if tokens <= max_tokens:
            result = truncated
            left = mid
        else:
            right = mid - 1

    return result


def truncate_smart(text, 
                   max_tokens, 
                   memory_obj):
    """Truncate text keeping beginning and end for context"""
    current_tokens = memory_obj.estimate_tokens(text)

    if current_tokens <= max_tokens:
        return text

    # Keep first 40% and last 40% of the token budget
    part_tokens = int(max_tokens * 0.4)

    # Find how many characters give us roughly part_tokens
    # This is approximate since we can't easily reverse the tokenization
    estimated_chars_per_token = len(text) / current_tokens
    chars_each_side = int(part_tokens * estimated_chars_per_token)

    return f"{text[:chars_each_side]}... [content truncated] ...{text[-chars_each_side:]}"


def generate_labels(topic: str, 
                    theme: str, 
                    domain: str) -> list[str]:
    
    if domain == "general":
        prompt = label_generation_prompt_template.format(topic, theme)
    elif domain == "coding":
        prompt = coding_label_generation_prompt_template.format(topic, theme)
    elif domain == "math":
        prompt = math_label_generation_prompt_template.format(topic, theme)

    response = llama_llm.invoke(prompt).content

    return response


def extract_labels(labels_text: str) -> List[Dict]:
    HEADER_RE = re.compile(
        r"""
        ^\*{0,2}              
        (?P<title>.+? Labels) 
        :\*{0,2}$          
        """,
        re.VERBOSE,
    )

    lines = [ln.strip() for ln in labels_text.splitlines() if ln.strip()]
    records, current = [], None

    for idx, ln in enumerate(lines):
        header = HEADER_RE.match(ln)
        if header:
            if current:
                records.append(current)
            current = {
                "category": header.group("title"),
                "description": "",
                "sublabels": [],
            }
            continue

        if ln.startswith("-") and current:
            bullet = ln.lstrip("- ").strip()

            next_is_bullet = (
                idx + 1 < len(lines) and lines[idx + 1].startswith("-")
            )

            if not current["description"] and next_is_bullet:
                current["description"] = bullet
            else:
                current["sublabels"] = [s.strip() for s in bullet.split(",")]

    if current:
        records.append(current)
    return records


def format_labels_for_llm(records):
    """Format labels in a clear, structured way for LLM processing"""
    formatted_labels = []

    for i, record in enumerate(records, 1):
        category = record['category'].replace(':', '').strip()
        description = record['description']
        sublabels = ', '.join(
            record['sublabels']) if record['sublabels'] else "General application"

        formatted_labels.append(
            f"{i}. LABEL CATEOGRY: {category}\n   LABEL DESCRIPTION: {description}\n   Focus Areas: {sublabels}")

    return "\n\n".join(formatted_labels)


def format_user_profile_for_llm(main_spec):
    """Format user profile in a clear, readable structure"""
    profile_text = f"""
    USER PROFILE:
    • Name: {main_spec['name']}
    • Age: {main_spec['age']} years old
    • Gender: {main_spec['gender'].title()}
    • Location: {main_spec['living location']}
    • Profession: {main_spec['job_title'].title()}

    PERSONALITY OVERVIEW:
    {main_spec['personality_traits']}
    """
    return profile_text.strip()


def format_relationships_for_llm(relationships):
    """Format relationships in a clear, hierarchical structure"""
    relationship_sections = []

    # Define relationship categories with descriptions
    relationship_types = {
        'parent': 'PARENTS & GUARDIANS',
        'partner': 'ROMANTIC PARTNER',
        'children': 'CHILDREN',
        'friends': 'CLOSE FRIENDS',
        'acquaintances': 'ACQUAINTANCES & COLLEAGUES'
    }

    for rel_type, section_title in relationship_types.items():
        if rel_type in relationships and relationships[rel_type]:
            people = []
            for person in relationships[rel_type]:
                if isinstance(person, dict) and 'name' in person:
                    people.append(
                        f"• {person['name']} ({person['gender']}, age {person['age']})")
                elif isinstance(person, (int, str)):
                    people.append(f"• [ID: {person}]")

            if people:
                relationship_sections.append(
                    f"{section_title}:\n" + "\n".join(people))

    return "\n\n".join(relationship_sections)


def get_unique_lines(raw: str, 
                     already: set[str]) -> list[str]:
    
    lines = [l.strip() for l in raw.splitlines() if l.strip()
             and not l.strip().startswith("###")]
    return [l for l in lines if l.lower() not in {s.lower() for s in already}]


def get_unique_messages(raw: str, 
                        already: set[str]) -> list[str]:
    """Extract messages using the separator specified in prompt"""

    # Remove completion marker
    content = re.sub(r'###\s*COMPLETE\s*###.*$', '', raw,
                     flags=re.IGNORECASE | re.DOTALL).strip()

    # Split by the separator
    messages = [msg.strip() for msg in content.split(
        '---MESSAGE_SEPARATOR---') if msg.strip()]

    # Filter duplicates
    unique_messages = []
    already_lower = {msg.lower() for msg in already}

    for msg in messages:
        if msg.lower() not in already_lower:
            unique_messages.append(msg)
            already_lower.add(msg.lower())

    return unique_messages


def extract_plan_bullets(plan_text: str) -> list[str]:
    """Extract individual bullets from plan text"""
    bullets = re.findall(
        r"• \*\*(.+?):\*\*(.+?)(?=• \*\*|\n|$)", plan_text, re.DOTALL)
    return [f"{label.strip()}: {content.strip()}" for label, content in bullets]


def distribute_bullets_across_batches(bullets: list[str], 
                                      num_sub_batches: int, 
                                      distrubtion_type: str) -> list[list[str]]:
    """Distribute bullets across sub-batches to ensure even coverage"""

    if distrubtion_type == "round-robin":
        sub_batches = [[] for _ in range(num_sub_batches)]

        for i, bullet in enumerate(bullets):
            sub_batches[i % num_sub_batches].append(bullet)

        return sub_batches
    elif distrubtion_type == "normal":
        n = len(bullets)
        q, r = divmod(n, num_sub_batches)
        batches = []
        start = 0
        for i in range(num_sub_batches):
            size = q + (1 if i < r else 0)
            batches.append(bullets[start: start + size])
            start += size
        return batches


# ================================ LABEL GENERATION ================================


def get_labels(topic: str, 
               theme: str, 
               domain: str) -> str:
    labels_text = generate_labels(topic=topic, theme=theme, domain=domain)
    labels = extract_labels(labels_text=labels_text)
    labels = format_labels_for_llm(labels)

    return labels

# ================================ PROFILE GENERATION ================================


def get_profile():
    main_spec, relationships = create_profile(
        all_profile_size=70, friends_size=5, acquaintances_size=5)
    main_spec = format_user_profile_for_llm(main_spec)
    relationships = format_relationships_for_llm(relationships)

    return main_spec, relationships


# ================================ PLAN GENERATION ================================


def generate_plans(topic: str, 
                   theme: str, 
                   timeline: str, 
                   num_batches: int,
                   num_bullets: int, 
                   labels: str, 
                   main_spec: str, 
                   relationships: str, 
                   llm_name: str,
                   save_address: str, 
                   input_address: str = None, 
                   domain: str = "general") -> List[str]:

    if input_address:
        with open(input_address, 'rb') as f:
            plans = pickle.load(f)

        return plans

    if domain == "general":
        plan_generation_prompt = plan_generation_prompt_profile_and_topic_given_detailed_template\
            .replace("<topic>", topic)\
            .replace("<theme>", theme)\
            .replace("<timeline>", timeline)\
            .replace("<num_batches>", str(num_batches))\
            .replace("<provided_labels>", str(labels))\
            .replace("<user_profile>", str(main_spec))\
            .replace("<user_relationships>", str(relationships))\
            .replace("<num_bullets>", str(num_bullets))

    elif domain == "coding":
        plan_generation_prompt = coding_plan_generation_prompt_detailed\
            .replace("<topic>", topic)\
            .replace("<theme>", theme)\
            .replace("<timeline>", timeline)\
            .replace("<num_batches>", str(num_batches))\
            .replace("<provided_labels>", str(labels))\
            .replace("<user_profile>", str(main_spec))\
            .replace("<num_bullets>", str(num_bullets))

    elif domain == "math":
        plan_generation_prompt = math_plan_generation_prompt_detailed\
            .replace("<topic>", topic)\
            .replace("<theme>", theme)\
            .replace("<timeline>", timeline)\
            .replace("<num_batches>", str(num_batches))\
            .replace("<provided_labels>", str(labels))\
            .replace("<user_profile>", str(main_spec))\
            .replace("<num_bullets>", str(num_bullets))

    if llm_name == "gpt":
        llm = gpt_llm
    elif llm_name == "qwen":
        llm = qwen_llm
    elif llm_name == "llama":
        llm = llama_llm

    plan_response = llm.invoke(plan_generation_prompt)
    plan_response = plan_response.content

    raw_batches = re.split(r'(BATCH \d+ PLAN)', plan_response)

    plans = []
    for i in range(1, len(raw_batches), 2):
        header = raw_batches[i].strip()
        content = raw_batches[i + 1].strip()
        plans.append(f"{header}\n{content}")

    with open(f'{save_address}.pickle', 'wb') as f:
        pickle.dump(plans, f)

    with open(f'{save_address}.txt', 'w', encoding='utf-8') as f:
        f.writelines(plan_response)

    return plans


def generate_detailed_plans(topic: str, 
                            theme: str, 
                            timeline: str, 
                            num_messages: int, 
                            batch_size: int, 
                            num_batches: int,
                            labels: str, 
                            main_spec: str, 
                            relationships: str, 
                            llm_name: str, 
                            save_address: str, 
                            input_address: str = None, 
                            domain: str = "general") -> List[str]:

    plans = []
    new_plans = []
    original_plan = ""
    if input_address:
        with open(input_address, 'rb') as f:
            plans = pickle.load(f)
    else:
        if domain == "general":
            plan_generation_prompt = plan_generation_prompt_profile_and_topic_given_template\
                .replace("<topic>", topic)\
                .replace("<theme>", theme)\
                .replace("<timeline>", timeline)\
                .replace("<total_messages>", str(num_messages))\
                .replace("<batch_size>", str(batch_size))\
                .replace("<num_batches>", str(num_batches))\
                .replace("<provided_labels>", str(labels))\
                .replace("<user_profile>", str(main_spec))\
                .replace("<user_relationships>", str(relationships))

        elif domain == "coding":
            plan_generation_prompt = coding_plan_generation_prompt\
                .replace("<topic>", topic)\
                .replace("<theme>", theme)\
                .replace("<timeline>", timeline)\
                .replace("<total_messages>", str(num_messages))\
                .replace("<batch_size>", str(batch_size))\
                .replace("<num_batches>", str(num_batches))\
                .replace("<provided_labels>", str(labels))\
                .replace("<user_profile>", str(main_spec))

        elif domain == "math":
            plan_generation_prompt = math_plan_generation_prompt\
                .replace("<topic>", topic)\
                .replace("<theme>", theme)\
                .replace("<timeline>", timeline)\
                .replace("<total_messages>", str(num_messages))\
                .replace("<batch_size>", str(batch_size))\
                .replace("<num_batches>", str(num_batches))\
                .replace("<provided_labels>", str(labels))\
                .replace("<user_profile>", str(main_spec))

        if llm_name == "gpt":
            llm = gpt_llm
        elif llm_name == "qwen":
            llm = qwen_llm
        elif llm_name == "llama":
            llm = llama_llm

        plan_response = llm.invoke(plan_generation_prompt)
        plan_response = plan_response.content

        raw_batches = re.split(r'(BATCH \d+ PLAN)', plan_response)

        for i in range(1, len(raw_batches), 2):
            header = raw_batches[i].strip()
            content = raw_batches[i + 1].strip()
            plans.append(f"{header}\n{content}")
            original_plan += f"{header}\n{content}"

    for plan in plans:
        original_plan += plan + "\n\n"

    if domain == "general":
        plan_generation_prompt = convert_broad_plan_to_detailed_plan_prompt\
            .replace("<original_plan>", original_plan)\
            .replace("<topic>", topic)\
            .replace("<theme>", theme)\
            .replace("<timeline>", timeline)\
            .replace("<user_profile>", str(main_spec))\
            .replace("<user_relationships>", str(relationships))\

        if llm_name == "gpt":
            llm = gpt_llm
        elif llm_name == "qwen":
            llm = qwen_llm
        elif llm_name == "llama":
            llm = llama_llm

        plan_response = llm.invoke(plan_generation_prompt)
        plan_response = plan_response.content

        raw_batches = re.split(r'(BATCH \d+ PLAN)', plan_response)

        for i in range(1, len(raw_batches), 2):
            header = raw_batches[i].strip()
            content = raw_batches[i + 1].strip()
            new_plans.append(f"{header}\n{content}")

        with open(f'{save_address}.pickle', 'wb') as f:
            pickle.dump(plans, f)

        with open(f'{save_address}.txt', 'w', encoding='utf-8') as f:
            f.writelines(plan_response)

# ================================ PLAN REVISION ================================


def plan_revision(topic: str, 
                  theme: str, 
                  plans: list, 
                  llm_name: str, 
                  save_address: str) -> List[str]:
    
    plan_refinement_prompt = plan_revision_prompt_template\
        .replace("<topic>", topic)\
        .replace("<theme>", theme)\
        .replace("<generated_plans>", "\n\n".join(plans))

    if llm_name == "gpt":
        llm = gpt_llm
    elif llm_name == "qwen":
        llm = qwen_llm
    elif llm_name == "llama":
        llm = llama_llm

    new_plan = llm.invoke(plan_refinement_prompt).content

    raw_batches = re.split(r'(BATCH \d+ PLAN)', new_plan)

    plans = []
    for i in range(1, len(raw_batches), 2):
        header = raw_batches[i].strip()
        content = raw_batches[i + 1].strip()
        plans.append(f"{header}\n{content}")

    with open(f'{save_address}.pickle', 'wb') as f:
        pickle.dump(plans, f)

    with open(f'{save_address}.txt', 'w', encoding='utf-8') as f:
        f.writelines(new_plan)

    return plans

# ================================ PLAN SPECIAL BULLETS ================================


def add_special_bullets_to_plan(plan_address: str,
                                num_bullets: int,
                                llm_name: str) -> None:

    if llm_name == "gpt":
        llm = gpt_llm
    elif llm_name == "qwen":
        llm = qwen_llm
    elif llm_name == "llama":
        llm = llama_llm

    with open(plan_address+".pickle", 'rb') as f:
        plan = pickle.load(f)

    plan_text = "\n\n".join(plan)

    prompt = add_special_bulletpoints_to_plan_implicit\
        .replace("<plan>", plan_text)\
        .replace("<num_bullets>", str(num_bullets))

    response = llm.invoke(prompt).content

    with open(plan_address+"_new.txt", 'w', encoding='utf-8') as f:
        f.writelines(response)

    raw_batches = re.split(r'(BATCH \d+ PLAN)', response)

    plans = []
    for i in range(1, len(raw_batches), 2):
        header = raw_batches[i].strip()
        content = raw_batches[i + 1].strip()
        plans.append(f"{header}\n{content}")

    with open(plan_address+"_new.pickle", 'wb') as f:
        pickle.dump(plans, f)

# ================================ USER MESSAGES GENERATION ================================


def estimate_token_count(text):
    return int(len(text) / 3.7)


def trim_previous_plans(previous_plans, 
                        max_tokens=4000):
    """
    Trim previous plans to stay within token limit.
    Keeps most recent plans and adds summary of removed ones.
    """
    if not previous_plans:
        return previous_plans

    batch_plans = previous_plans.split("BATCH")
    batch_plans = [f"BATCH{plan}" for plan in batch_plans if plan.strip()]

    if not batch_plans:
        return previous_plans

    kept_plans = []
    current_tokens = 0

    for plan in reversed(batch_plans):
        plan_tokens = estimate_token_count(plan)
        if current_tokens + plan_tokens < max_tokens:
            kept_plans.insert(0, plan)
            current_tokens += plan_tokens
        else:
            break

    if len(kept_plans) < len(batch_plans):
        removed_count = len(batch_plans) - len(kept_plans)
        summary = f"[Previous {removed_count} batch plans omitted for context length. Showing most recent {len(kept_plans)} plans.]\n\n"
        return summary + "\n".join(kept_plans)

    return previous_plans


def user_messages_generation(topic: str, 
                             theme: str, 
                             plans: list, 
                             num_batches: int,
                             sub_batches_per_batch: int, 
                             sub_batch_size: int, 
                             batch_size: int, 
                             llm_name: str, 
                             save_address: str, 
                             domain: str, 
                             sepcial_bullets: bool = False) -> None:
    all_messages = []
    global_history = set()

    if llm_name == "gpt":
        llm = gpt_llm
    elif llm_name == "qwen":
        llm = qwen_llm
    elif llm_name == "llama":
        llm = llama_llm

    temp_sub_batches_per_batch = sub_batches_per_batch

    for batch_idx in range(num_batches):
        print(f"Processing Batch {batch_idx + 1}/{num_batches}")

        # Get context
        past_plans = "\n\n".join(plans[:batch_idx][::-1])
        cur_plan = plans[batch_idx]

        # Extract bullets from current plan
        plan_bullets = extract_plan_bullets(cur_plan)

        time_anchor = extract_time_anchor(plan_text=plan_bullets[0])

        sepcial_bullets_list = []
        if sepcial_bullets:
            sepcial_bullets_list = plan_bullets[-3:]
            plan_bullets = plan_bullets[:-3]

        sub_batches_per_batch = temp_sub_batches_per_batch
        # Distribute bullets across sub-batches
        bullet_groups = distribute_bullets_across_batches(
            plan_bullets, sub_batches_per_batch, distrubtion_type="normal")

        if sepcial_bullets:
            bullet_groups.append(sepcial_bullets_list)
            sub_batches_per_batch += 1

        batch_lines = []
        batch_history = []

        for sub_batch_idx in range(sub_batches_per_batch):
            print(f"  Sub-batch {sub_batch_idx + 1}/{sub_batches_per_batch}")

            focused_bullets = "\n".join(
                f"{index+1}) {bullet}" for index, bullet in enumerate(bullet_groups[sub_batch_idx]))
            batch_history_text = "\n".join(
                batch_history) if batch_history else "(none)"

            previous_sub_batch_plans = ""
            for bullets in bullet_groups[:sub_batch_idx]:
                previous_sub_batch_plans += "\n".join(
                    f"• {bullet}" for bullet in bullets) + "\n\n"

            if sepcial_bullets and (sub_batch_idx == sub_batches_per_batch - 1):
                # if "Logical Contradiction:" in bullet_groups[sub_batch_idx][2]:
                #     temp_contradiction = bullet_groups[sub_batch_idx][2].split("Logical Contradiction:")[1].strip()
                temp_sub_batch_size = 2
                temp_focused_bullets = bullet_groups[sub_batch_idx][0] + \
                    "\n\n" + bullet_groups[sub_batch_idx][2]
                temp_instruction = bullet_groups[sub_batch_idx][1]

            else:
                temp_sub_batch_size = sub_batch_size

            if domain == "general":
                if temp_sub_batch_size == 2 and (sub_batch_idx == sub_batches_per_batch - 1):
                    system_prompt = message_generation_prompt_focused_template_special\
                        .replace("<TOPIC>", topic)\
                        .replace("<THEME>", theme)\
                        .replace("<FOCUSED_BULLETS>", temp_focused_bullets)\
                        .replace("<PREVIOUS_SUB_BATCH_PLANS>", "none" if previous_sub_batch_plans else "(none)")\
                        .replace("<SUB_BATCH_SIZE>", str(temp_sub_batch_size))\
                        .replace("<PREVIOUS_BATCH_PLANS>", past_plans if past_plans else "(none)")
                else:
                    system_prompt = message_generation_prompt_focused_template\
                        .replace("<TOPIC>", topic)\
                        .replace("<THEME>", theme)\
                        .replace("<FOCUSED_BULLETS>", focused_bullets)\
                        .replace("<PREVIOUS_SUB_BATCH_PLANS>", previous_sub_batch_plans if previous_sub_batch_plans else "(none)")\
                        .replace("<SUB_BATCH_SIZE>", str(temp_sub_batch_size))\
                        .replace("<PREVIOUS_BATCH_PLANS>", past_plans if past_plans else "(none)")

            elif domain == "coding":
                system_prompt = coding_message_generation_prompt\
                    .replace("<TOPIC>", topic)\
                    .replace("<THEME>", theme)\
                    .replace("<FOCUSED_BULLETS>", focused_bullets)\
                    .replace("<PREVIOUS_SUB_BATCH_PLANS>", previous_sub_batch_plans if previous_sub_batch_plans else "(none)")\
                    .replace("<SUB_BATCH_SIZE>", str(temp_sub_batch_size))\
                    .replace("<PREVIOUS_BATCH_PLANS>", past_plans if past_plans else "(none)")

            elif domain == "math":
                system_prompt = math_message_generation_prompt\
                    .replace("<TOPIC>", topic)\
                    .replace("<THEME>", theme)\
                    .replace("<FOCUSED_BULLETS>", focused_bullets)\
                    .replace("<PREVIOUS_SUB_BATCH_PLANS>", previous_sub_batch_plans if previous_sub_batch_plans else "(none)")\
                    .replace("<SUB_BATCH_SIZE>", str(temp_sub_batch_size))\
                    .replace("<PREVIOUS_BATCH_PLANS>", past_plans if past_plans else "(none)")

            sub_batch_lines = []
            retries = 0

            while len(sub_batch_lines) < temp_sub_batch_size and retries < 3:
                messages = [
                    SystemMessage(content=system_prompt),
                ]

                try:
                    if retries > 0:
                        system_prompt.replace(
                            "<BATCH_HISTORY>", "\n\n".join(sub_batch_lines))
                        messages = [
                            SystemMessage(content=system_prompt),
                        ]

                    raw = llm.invoke(messages, max_tokens=6000).content

                    if domain == "general":
                        new_lines = get_unique_lines(
                            raw, global_history | set(batch_lines))
                    elif domain == "coding" or domain == "math":
                        new_lines = get_unique_messages(
                            raw, global_history | set(batch_lines))

                    # Additional filtering for this sub-batch to avoid immediate repetition
                    new_lines = [line for line in new_lines if line.lower() not in {
                        l.lower() for l in sub_batch_lines}]

                    sub_batch_lines.extend(
                        new_lines[:temp_sub_batch_size - len(sub_batch_lines)])
                    retries += 1

                except Exception as e:
                    print(f"Error in sub-batch {sub_batch_idx}: {e}")
                    retries += 1

            if temp_sub_batch_size == 2 and (sub_batch_idx == sub_batches_per_batch - 1):
                if "User Instruction:" in temp_instruction:
                    temp_instruction = temp_instruction.split(
                        "User Instruction:")[1].strip()

                sub_batch_lines.insert(1, temp_instruction)

            questions = ""
            for index, question in enumerate(sub_batch_lines):
                questions += f"{index+1}) {question} \n\n"

            prompt = f"""Match each question to its corresponding bulletpoint.
                    Questions:
                    {questions}

                    Bulletpoints:
                    {focused_bullets}

                    Instructions:
                    - Process each question from Q1 to Q{len(sub_batch_lines)} in order
                    - For each question, write: [question text] ->-> [bulletpoint number or N/A]
                    - Use exactly ONE number after ->->
                    - If a question doesn't match any bulletpoint, use N/A
                    - Separate questions with: ---MESSAGE_SEPARATOR---
                    - Do NOT add separator after the last question
                    - List each question only ONCE
                    - Stop after processing all questions

                    Output format example:
                    question one ->-> 1 ---MESSAGE_SEPARATOR--- question two ->-> N/A ---MESSAGE_SEPARATOR--- question three ->-> 2

                    Begin matching:"""

            response = llm.invoke(prompt).content

            batch_number = batch_idx+1
            previous_bullet_num = 0
            for i in range(sub_batch_idx):
                previous_bullet_num += len(bullet_groups[i])

            sub_batch_lines = []
            for question in response.split("---MESSAGE_SEPARATOR---"):
                if "->->" in question:
                    question_temp = question.split("->->")[0].strip()
                    bullet_num = question.split("->->")[1].strip()
                    if bullet_num == "N/A":
                        new_question = question_temp + \
                            " ->-> " + f"{batch_number},N/A"
                    else:
                        if bullet_num.isdigit():
                            new_question = question_temp + " ->-> " + \
                                f"{batch_number},{previous_bullet_num+int(bullet_num)}"
                        else:
                            new_question = question + \
                                " ->-> " + f"{batch_number},N/A"

                    sub_batch_lines.append(new_question)
                elif question.strip() != "":
                    new_question = question + " ->-> " + f"{batch_number},N/A"
                    sub_batch_lines.append(new_question)

            temp_sub_batch_lines = []
            for question in sub_batch_lines:
                formatted_question = question
                if ")" in question:
                    formatted_question = question.split(") ", 1)[1]
                temp_sub_batch_lines.append(formatted_question)

            # Add successful lines to main batch
            batch_lines.extend(temp_sub_batch_lines)
            batch_history.extend(temp_sub_batch_lines)

            print(
                f"  Generated {len(temp_sub_batch_lines)} lines for sub-batch {sub_batch_idx + 1}")

        # Final cleanup and deduplication for the entire batch
        final_batch_lines = []
        seen_lower = set()

        for line in batch_lines:
            line_lower = line.lower()
            # More sophisticated similarity check
            is_similar = any(
                len(set(line_lower.split()) & set(existing.split())) /
                max(len(line_lower.split()), len(existing.split())) > 0.7
                for existing in seen_lower
            )

            if not is_similar:
                final_batch_lines.append(line)
                seen_lower.add(line_lower)

        final_object = {
            "time_anchor": time_anchor,
            "messages": [final_batch_lines]
        }
        # Ensure we don't exceed batch size
        all_messages.append(final_object)
        global_history.update(l.lower()
                              for l in final_batch_lines)

        print(
            f"Batch {batch_idx + 1} complete: {len(final_batch_lines)} messages")

    # Save results
    with open(save_address, 'wb') as f:
        pickle.dump(all_messages, f)

    print(
        f"Generation complete. Total messages: {sum(len(batch) for batch in all_messages)}")


def user_messages_generation_fast(topic: str, 
                                  theme: str, 
                                  plans: list,
                                  num_batches: int,
                                  sub_batches_per_batch: int, 
                                  sub_batch_size: int, 
                                  batch_size: int, 
                                  llm_name: str, 
                                  save_address: str, 
                                  domain: str, 
                                  sepcial_bullets: bool = False) -> None:
    all_messages = []
    global_history = set()

    if llm_name == "gpt":
        llm = gpt_llm
    elif llm_name == "qwen":
        llm = qwen_llm
    elif llm_name == "llama":
        llm = llama_llm

    temp_sub_batches_per_batch = sub_batches_per_batch

    for batch_idx in range(num_batches):
        print(f"Processing Batch {batch_idx + 1}/{num_batches}")

        # Get context
        past_plans = "\n\n".join(plans[:batch_idx][::-1])
        cur_plan = plans[batch_idx]

        # Extract bullets from current plan
        plan_bullets = extract_plan_bullets(cur_plan)
    
        time_anchor = extract_time_anchor(plan_text=plan_bullets[0])

        sepcial_bullets_list = []
        if sepcial_bullets:
            sepcial_bullets_list = plan_bullets[-3:]
            plan_bullets = plan_bullets[:-3]

        sub_batches_per_batch = temp_sub_batches_per_batch
        # Distribute bullets across sub-batches
        bullet_groups = distribute_bullets_across_batches(
            plan_bullets, sub_batches_per_batch, distrubtion_type="normal")

        if sepcial_bullets:
            bullet_groups.append(sepcial_bullets_list)
            sub_batches_per_batch += 1

        batch_lines = []
        batch_history = []

        for sub_batch_idx in range(sub_batches_per_batch):
            print(f"  Sub-batch {sub_batch_idx + 1}/{sub_batches_per_batch}")

            batch_number = batch_idx+1
            previous_bullet_num = 0
            for i in range(sub_batch_idx):
                previous_bullet_num += len(bullet_groups[i])

            focused_bullets = "\n".join(
                f"{previous_bullet_num+index+1}) {bullet}" for index, bullet in enumerate(bullet_groups[sub_batch_idx]))
            batch_history_text = "\n".join(
                batch_history) if batch_history else "(none)"

            previous_sub_batch_plans = ""
            for bullets in bullet_groups[:sub_batch_idx]:
                previous_sub_batch_plans += "\n".join(
                    f"• {bullet}" for bullet in bullets) + "\n\n"

            if sepcial_bullets and (sub_batch_idx == sub_batches_per_batch - 1):
                # if "Logical Contradiction:" in bullet_groups[sub_batch_idx][2]:
                #     temp_contradiction = bullet_groups[sub_batch_idx][2].split("Logical Contradiction:")[1].strip()
                temp_sub_batch_size = 2
                temp_focused_bullets = f"{previous_bullet_num+1}) " + bullet_groups[sub_batch_idx][0] + \
                    "\n\n" + f"{previous_bullet_num+3}) " + \
                    bullet_groups[sub_batch_idx][2]
                temp_instruction = bullet_groups[sub_batch_idx][1] + \
                    f" ->-> {previous_bullet_num+2}"

            else:
                temp_sub_batch_size = sub_batch_size

            if domain == "general":
                if temp_sub_batch_size == 2 and (sub_batch_idx == sub_batches_per_batch - 1):
                    base_prompt = message_generation_prompt_focused_template_fast_special
                    focused_bullets_to_use = temp_focused_bullets
                else:
                    base_prompt = message_generation_prompt_focused_template_fast
                    focused_bullets_to_use = focused_bullets

                total_context = (
                    len(base_prompt) +
                    len(topic) +
                    len(theme) +
                    len(focused_bullets_to_use) +
                    len(previous_sub_batch_plans or "") +
                    len(past_plans or "") +
                    len(str(temp_sub_batch_size))
                )

                total_tokens = total_context // 3.7
                if total_tokens > 12500:
                    past_plans = trim_previous_plans(
                        past_plans, max_tokens=4000)

                    total_context_after_trim = (
                        len(base_prompt) +
                        len(topic) +
                        len(theme) +
                        len(focused_bullets_to_use) +
                        len(previous_sub_batch_plans or "") +
                        len(past_plans or "") +
                        len(str(temp_sub_batch_size))
                    )

                    total_tokens = total_context_after_trim // 3.7
                    if total_tokens > 12500:
                        past_plans = trim_previous_plans(
                            past_plans, max_tokens=2000)
                        if previous_sub_batch_plans and len(previous_sub_batch_plans) > 8000:
                            previous_sub_batch_plans = "...[Earlier sub-batches trimmed]\n" + \
                                previous_sub_batch_plans[-8000:]

                if temp_sub_batch_size == 2 and (sub_batch_idx == sub_batches_per_batch - 1):
                    system_prompt = message_generation_prompt_focused_template_fast_special\
                        .replace("<TOPIC>", topic)\
                        .replace("<THEME>", theme)\
                        .replace("<FOCUSED_BULLETS>", temp_focused_bullets)\
                        .replace("<PREVIOUS_SUB_BATCH_PLANS>", "none" if previous_sub_batch_plans else "(none)")\
                        .replace("<SUB_BATCH_SIZE>", str(temp_sub_batch_size))\
                        .replace("<PREVIOUS_BATCH_PLANS>", past_plans if past_plans else "(none)")
                else:
                    system_prompt = message_generation_prompt_focused_template_fast\
                        .replace("<TOPIC>", topic)\
                        .replace("<THEME>", theme)\
                        .replace("<FOCUSED_BULLETS>", focused_bullets)\
                        .replace("<PREVIOUS_SUB_BATCH_PLANS>", previous_sub_batch_plans if previous_sub_batch_plans else "(none)")\
                        .replace("<SUB_BATCH_SIZE>", str(temp_sub_batch_size))\
                        .replace("<PREVIOUS_BATCH_PLANS>", past_plans if past_plans else "(none)")

            elif domain == "coding":
                total_context = (
                    len(coding_message_generation_prompt_fast) +
                    len(topic) +
                    len(theme) +
                    len(focused_bullets) +
                    len(previous_sub_batch_plans or "") +
                    len(past_plans or "") +
                    len(str(temp_sub_batch_size))
                )

                total_tokens = total_context // 3.7
                if total_tokens > 12500:
                    past_plans = trim_previous_plans(
                        past_plans, max_tokens=4000)

                system_prompt = coding_message_generation_prompt_fast\
                    .replace("<TOPIC>", topic)\
                    .replace("<THEME>", theme)\
                    .replace("<FOCUSED_BULLETS>", focused_bullets)\
                    .replace("<PREVIOUS_SUB_BATCH_PLANS>", previous_sub_batch_plans if previous_sub_batch_plans else "(none)")\
                    .replace("<SUB_BATCH_SIZE>", str(temp_sub_batch_size))\
                    .replace("<PREVIOUS_BATCH_PLANS>", past_plans if past_plans else "(none)")

            elif domain == "math":
                total_context = (
                    len(math_message_generation_prompt_fast) +
                    len(topic) +
                    len(theme) +
                    len(focused_bullets) +
                    len(previous_sub_batch_plans or "") +
                    len(past_plans or "") +
                    len(str(temp_sub_batch_size))
                )

                total_tokens = total_context // 3.7
                if total_tokens > 12500:
                    past_plans = trim_previous_plans(
                        past_plans, max_tokens=4000)

                system_prompt = math_message_generation_prompt_fast\
                    .replace("<TOPIC>", topic)\
                    .replace("<THEME>", theme)\
                    .replace("<FOCUSED_BULLETS>", focused_bullets)\
                    .replace("<PREVIOUS_SUB_BATCH_PLANS>", previous_sub_batch_plans if previous_sub_batch_plans else "(none)")\
                    .replace("<SUB_BATCH_SIZE>", str(temp_sub_batch_size))\
                    .replace("<PREVIOUS_BATCH_PLANS>", past_plans if past_plans else "(none)")

            sub_batch_lines = []
            retries = 0

            while len(sub_batch_lines) < temp_sub_batch_size and retries < 3:
                messages = [
                    SystemMessage(content=system_prompt),
                ]

                try:
                    if retries > 0:
                        if estimate_token_count(system_prompt + "\n\n".join(sub_batch_lines)) < 12800:

                            system_prompt.replace(
                                "<BATCH_HISTORY>", "\n\n".join(sub_batch_lines))
                            messages = [
                                SystemMessage(content=system_prompt),
                            ]

                    raw = llm.invoke(messages, max_tokens=3000).content

                    if domain == "general":
                        new_lines = get_unique_lines(
                            raw, global_history | set(batch_lines))
                    elif domain == "coding" or domain == "math":
                        new_lines = get_unique_messages(
                            raw, global_history | set(batch_lines))

                    # Additional filtering for this sub-batch to avoid immediate repetition
                    new_lines = [line for line in new_lines if line.lower() not in {
                        l.lower() for l in sub_batch_lines}]

                    sub_batch_lines.extend(
                        new_lines[:temp_sub_batch_size - len(sub_batch_lines)])
                    retries += 1

                except Exception as e:
                    print(f"Error in sub-batch {sub_batch_idx}: {e}")
                    error_file_address = save_address.split(".pickle")[
                        0] + ".txt"
                    with open(error_file_address, "a") as f:
                        f.write(f"{e}\n")
                    retries += 1

            if temp_sub_batch_size == 2 and (sub_batch_idx == sub_batches_per_batch - 1):
                temp_instruction = temp_instruction.split(
                    "User Instruction:")[1].strip()
                sub_batch_lines.insert(1, temp_instruction)

            temp_sub_batch_lines = []
            for question in sub_batch_lines:
                formatted_question = question
                formatted_question = re.sub(r'^\d+\)\s*', '', question)
                temp_sub_batch_lines.append(formatted_question)

            final_sub_batch_lines = []
            for question in temp_sub_batch_lines:
                if "->->" in question:
                    bullet_number = question.split("->->")[1].strip()
                    if len(bullet_number) > 3:
                        print()
                    index = f"{batch_idx+1},{bullet_number}"
                    temp_question = question.split(
                        "->->")[0].strip() + " ->-> " + index
                else:
                    index = f"{batch_idx+1},N/A"
                    temp_question = question + " ->-> " + index

                final_sub_batch_lines.append(temp_question)

            # Add successful lines to main batch
            batch_lines.extend(final_sub_batch_lines)
            batch_history.extend(final_sub_batch_lines)

            print(
                f"  Generated {len(final_sub_batch_lines)} lines for sub-batch {sub_batch_idx + 1}")

        # Final cleanup and deduplication for the entire batch
        final_batch_lines = []
        seen_lower = set()

        for line in batch_lines:
            line_lower = line.lower()
            # More sophisticated similarity check
            is_similar = any(
                len(set(line_lower.split()) & set(existing.split())) /
                max(len(line_lower.split()), len(existing.split())) > 0.7
                for existing in seen_lower
            )

            if not is_similar:
                final_batch_lines.append(line)
                seen_lower.add(line_lower)

        # Ensure we don't exceed batch size
        final_object = {
            "time_anchor": time_anchor,
            "messages": [final_batch_lines]
        }
        all_messages.append(final_object)
        global_history.update(l.lower()
                              for l in final_batch_lines)

        print(
            f"Batch {batch_idx + 1} complete: {len(final_batch_lines)} messages")

    # Save results
    with open(save_address, 'wb') as f:
        pickle.dump(all_messages, f)

    print(
        f"Generation complete. Total messages: {sum(len(batch) for batch in all_messages)}")

# ================================ ANSWER GENERATION ================================


def check_include_questions(assistant_response: str,
                            llm) -> bool:

    prompt = check_include_question_template\
        .replace("<assistant_response>", assistant_response)

    response = llm.invoke(prompt).content.strip().lower()

    if "yes" in response:
        return True
    else:
        return False


def check_include_questions_safe(assistant_response,
                                 assistant_memory,
                                 llm,
                                 max_tokens=25000):

    response_tokens = assistant_memory.estimate_tokens(assistant_response)
    if response_tokens > max_tokens:
        assistant_response = truncate_to_tokens(
            assistant_response, max_tokens, assistant_memory)

    return check_include_questions(assistant_response=assistant_response, llm=llm)


def check_need_followup(assistant_response: str,
                        messages_history: list,
                        topic: str,
                        theme: str,
                        llm) -> bool:

    formatted_history = "\n".join([
        f"USER: {msg}" if i % 2 == 0 else f"ASSISTANT: {msg}"
        for i, msg in enumerate(messages_history)
    ])

    prompt = check_need_followup_template\
        .replace("<topic>", topic)\
        .replace("<theme>", theme)\
        .replace("<formatted_history>", formatted_history)\
        .replace("<assistant_response>", assistant_response)

    response = llm.invoke(prompt).content.strip().lower()

    if "yes" in response:
        return True
    else:
        return False


def check_need_followup_safe(assistant_response,
                             assistant_memory,
                             messages_history,
                             topic,
                             theme,
                             llm,
                             max_tokens=25000):

    # First, check if assistant_response alone is too large
    assistant_response_tokens = assistant_memory.estimate_tokens(
        assistant_response)
    topic_theme_tokens = assistant_memory.estimate_tokens(f"{topic}{theme}")

    # If assistant_response is too large, truncate it first
    # Reserve half for response, half for history
    max_response_tokens = (max_tokens - 1000) // 2

    if assistant_response_tokens > max_response_tokens:
        # Truncate assistant_response to fit
        assistant_response = truncate_to_tokens(
            assistant_response,
            max_response_tokens,
            assistant_memory
        )
        assistant_response_tokens = assistant_memory.estimate_tokens(
            assistant_response)

    # Calculate remaining budget for history
    base_tokens = assistant_response_tokens + topic_theme_tokens
    available_for_history = max_tokens - base_tokens - 1000  # Buffer

    # If we've already exceeded the limit with just base content
    if available_for_history <= 0:
        print(
            f"Warning: Base content alone uses {base_tokens} tokens, exceeding limit")
        # Try to call with minimal content
        return check_need_followup(
            # Aggressive truncation
            assistant_response=assistant_response[:1000] + "...[truncated]",
            messages_history=[],  # No history
            topic=topic[:100] if len(topic) > 100 else topic,
            theme=theme[:100] if len(theme) > 100 else theme,
            llm=llm
        )

    # Truncate history if needed
    if messages_history:
        history_tokens = sum(assistant_memory.estimate_tokens(
            msg.get("content", "")) for msg in messages_history
        )

        if history_tokens > available_for_history:
            # Keep only recent messages that fit
            truncated_history = []
            current_tokens = 0

            for msg in reversed(messages_history):
                msg_tokens = assistant_memory.estimate_tokens(
                    msg.get("content", ""))
                if current_tokens + msg_tokens < available_for_history:
                    truncated_history.insert(0, msg)
                    current_tokens += msg_tokens
                else:
                    # Try to include a truncated version of this message
                    remaining_tokens = available_for_history - current_tokens
                    if remaining_tokens > 100:  # Only if we have reasonable space
                        truncated_msg = msg.copy()
                        truncated_msg["content"] = truncate_to_tokens(
                            msg.get("content", ""),
                            remaining_tokens,
                            assistant_memory
                        )
                        truncated_history.insert(0, truncated_msg)
                    break

            messages_history = truncated_history

            print(
                f"Truncated history from {history_tokens} to {current_tokens} tokens")

    # Final safety check
    total_tokens = (
        assistant_memory.estimate_tokens(assistant_response) +
        assistant_memory.estimate_tokens(f"{topic}{theme}") +
        sum(assistant_memory.estimate_tokens(msg.get("content", ""))
            for msg in messages_history)
    )

    if total_tokens > max_tokens:
        print(
            f"Warning: Total tokens ({total_tokens}) still exceed limit ({max_tokens})")

    return check_need_followup(
        assistant_response=assistant_response,
        messages_history=messages_history,
        topic=topic,
        theme=theme,
        llm=llm
    )


def format_history_messages(message_history: list) -> str:
    history_text = ""
    for message in message_history:
        if message["role"] == "user":
            history_text += f"You: {message["content"]}" + "\n\n"
        elif message["role"] == "assistant":
            history_text += f"AI Assistant: {message["content"]}" + "\n\n"

    return history_text


def answer_generation(input_address: str,
                      output_address: str,
                      plans_address: str,
                      topic: str,
                      theme: str,
                      llm,
                      previous_plans_summary: str = ""):

    start = time.perf_counter()

    if not os.path.exists(input_address):
        raise FileNotFoundError(f"Input file not found: {input_address}")
    if not os.path.exists(plans_address):
        raise FileNotFoundError(f"Plans file not found: {plans_address}")

    with open(plans_address, 'rb') as f:
        plans = pickle.load(f)

    with open(input_address, 'rb') as f:
        batches = pickle.load(f)

    all_messages = []
    id = 0

    if os.path.isfile(output_address):
        with open(output_address, 'rb') as f:
            messages = pickle.load(f)
            all_messages = messages

    for batch_index, batch in enumerate(batches[len(all_messages):], start=len(all_messages)):
        try:
            previous_plans = ""
            for i in range(batch_index):
                plan = extract_plan_bullets(plan_text=plans[i])
                plan = "\n\n".join(plan)
                previous_plans += plan + "\n\n\n"

            current_plan = ""
            plan = extract_plan_bullets(plan_text=plans[batch_index])
            plan = "\n\n".join(plan)
            current_plan += plan + "\n\n\n"

        except Exception as e:
            print(f"Error extracting plan for batch {batch_index}: {str(e)}")

        if batch_index == 0:
            ai_assitant_system_prompt = ai_assistant_llm_template\
                .replace("<topic>", "N/A")\
                .replace("<theme>", "N/A")\
                .replace("<previous_plans_summary>", previous_plans_summary)\
                .replace("<previous_batches>", "N/A")
        else:
            ai_assitant_system_prompt = ai_assistant_llm_template\
                .replace("<topic>", topic)\
                .replace("<theme>", theme)\
                .replace("<previous_plans_summary>", previous_plans_summary)\
                .replace("<previous_batches>", previous_plans)

        try:
            assistant_prompt_tokens = get_token_number(
                ai_assitant_system_prompt)
            assistant_max_tokens = 28000 - assistant_prompt_tokens

            assistant_memory = ConversationSummaryBuffer(
                llm=llm,
                max_tokens=assistant_max_tokens,
                recent_messages_count=10,
                max_summary_tokens=1000
            )

            user_memory = ConversationSummaryBuffer(
                llm=llm,
                max_tokens=19000,
                recent_messages_count=10,
                max_summary_tokens=2000
            )
        except NameError:
            print("ConversationSummaryBuffer or llm not defined")
            continue
        except Exception as e:
            print(f"Error initializing memory objects: {str(e)}")
            continue

        ai_assistant_llm_messages_history = [
            {"role": "system", "content": ai_assitant_system_prompt}
        ]
        user_llm_messages_history = []

        ai_assitant_llm = llm
        user_llm = llm

        try:
            messages = batch['messages'][0]
            time_anchor = batch['time_anchor']
        except (KeyError, IndexError, TypeError) as e:
            print(
                f"Error extracting messages from batch {batch_index}: {str(e)}")
            continue
        
        for question_index, question in enumerate(messages):
            try:
                if "->->" in question:
                    batch_number = question.split("->->")[1].strip()
                    if "," in batch_number:
                        batch_number_index = batch_number.split(",")[0].strip()
                        bullet_number_index = batch_number.split(",")[
                            1].strip()
                        if bullet_number_index == "":
                            batch_number = batch_number_index + "," + "N/A"
                else:
                    batch_number = "N/A,N/A"

                elapsed = time.perf_counter() - start
                hms = time.strftime("%H:%M:%S", time.gmtime(elapsed))
                print(f"Elapsed time: {hms}")

                print(
                    f"Batch: {batch_index+1}/{len(batches)}, Question Index: {question_index+1}/{len(messages)}")

                # Add to user memory
                user_memory.add_message("user", question)
                assistant_memory.add_message(
                    "user", question + "Please respond only in English.")

                ai_assistant_llm_messages_history.append(
                    {"role": "assistant", "content": question}
                )

                # Get managed messages for assistant
                assistant_messages = assistant_memory.get_messages_for_llm(
                    ai_assitant_system_prompt)
                ai_assistant_response = ai_assitant_llm.invoke(
                    assistant_messages).content

                # Add response to memories
                assistant_memory.add_message(
                    "assistant", ai_assistant_response)
                user_memory.add_message("assistant", ai_assistant_response)

                ai_assistant_llm_messages_history.append(
                    {"role": "user", "content": ai_assistant_response}
                )

                if question_index == 0:
                    user_llm_messages_history.append(
                        {"role": "user", "id": id, "time_anchor": time_anchor, "index": batch_number,
                            "question_type": "main_question", "content": question}
                    )
                else:
                    user_llm_messages_history.append(
                        {"role": "user", "id": id, "index": batch_number,
                            "question_type": "main_question", "content": question}
                    )

                id += 1

                user_llm_messages_history.append(
                    {"role": "assistant", "id": id,
                        "content": ai_assistant_response}
                )
                id += 1

                num_questions = 0
                include_question = check_include_questions_safe(
                    assistant_response=ai_assistant_response, assistant_memory=assistant_memory, llm=llm)

                while include_question and num_questions < 2:
                    history_text = user_memory.get_conversation_history_text()

                    replacements = {
                        "current_batch_messages": history_text,
                        "topic": topic,
                        "theme": theme,
                        "previous_plans_summary": previous_plans_summary,
                        "previous_batches": previous_plans,
                        "current_plan": current_plan,
                        "ai_last_message": ai_assistant_response
                    }

                    user_system_prompt = prepare_prompt_within_budget(
                        user_llm_answer_question_template,
                        replacements,
                        user_memory,
                        max_tokens=27000
                    )

                    user_response = user_llm.invoke(user_system_prompt).content

                    # Add to memories
                    user_memory.add_message("user", user_response)
                    assistant_memory.add_message(
                        "user", user_response + "Please respond only in English.")

                    user_llm_messages_history.append(
                        {"role": "user", "id": id, "question_type": "answer_ai_question",
                            "content": user_response}
                    )
                    id += 1

                    ai_assistant_llm_messages_history.append(
                        {"role": "assistant", "content": user_response}
                    )

                    # Get managed messages for assistant
                    assistant_messages = assistant_memory.get_messages_for_llm(
                        ai_assitant_system_prompt)
                    ai_assistant_response = ai_assitant_llm.invoke(
                        assistant_messages).content

                    # Add to memories
                    user_memory.add_message("assistant", ai_assistant_response)
                    assistant_memory.add_message(
                        "assistant", ai_assistant_response)

                    user_llm_messages_history.append(
                        {"role": "assistant", "id": id,
                            "content": ai_assistant_response}
                    )
                    id += 1

                    ai_assistant_llm_messages_history.append(
                        {"role": "user", "content": ai_assistant_response}
                    )

                    include_question = check_include_questions_safe(
                        assistant_response=ai_assistant_response, assistant_memory=assistant_memory, llm=llm)

                    num_questions += 1

                messages_history = user_memory.get_messages_for_llm()

                need_followup = check_need_followup_safe(assistant_response=ai_assistant_response,
                                                         assistant_memory=assistant_memory,
                                                         messages_history=messages_history,
                                                         topic=topic, theme=theme, llm=llm)

                num_followup_questions = 0
                while need_followup and num_followup_questions < 2:
                    # Get managed conversation history from user memory
                    history_text = user_memory.get_conversation_history_text()

                    replacements = {
                        "current_batch_messages": history_text,
                        "topic": topic,
                        "theme": theme,
                        "previous_plans_summary": previous_plans_summary,
                        "previous_batches": previous_plans,
                        "current_plan": current_plan,
                        "ai_last_message": ai_assistant_response
                    }

                    user_system_prompt = prepare_prompt_within_budget(
                        user_llm_ask_followup_question_template,
                        replacements,
                        user_memory,
                        max_tokens=27000
                    )

                    user_response = user_llm.invoke(user_system_prompt).content

                    # Add to memories
                    user_memory.add_message("user", user_response)
                    assistant_memory.add_message(
                        "user", user_response + "Please respond only in English.")

                    user_llm_messages_history.append(
                        {"role": "user", "id": id, "question_type": "followup_question",
                            "content": user_response}
                    )
                    id += 1

                    ai_assistant_llm_messages_history.append(
                        {"role": "assistant", "content": user_response}
                    )

                    # Get managed messages for assistant
                    assistant_messages = assistant_memory.get_messages_for_llm(
                        ai_assitant_system_prompt)
                    ai_assistant_response = ai_assitant_llm.invoke(
                        assistant_messages).content

                    # Add to memories
                    user_memory.add_message("assistant", ai_assistant_response)
                    assistant_memory.add_message(
                        "assistant", ai_assistant_response)

                    user_llm_messages_history.append(
                        {"role": "assistant", "id": id,
                            "content": ai_assistant_response}
                    )
                    id += 1

                    ai_assistant_llm_messages_history.append(
                        {"role": "user", "content": ai_assistant_response}
                    )

                    num_followup_questions += 1

                    messages_history = user_memory.get_messages_for_llm()

                    need_followup = check_need_followup_safe(assistant_response=ai_assistant_response,
                                                             assistant_memory=assistant_memory,
                                                             messages_history=messages_history,
                                                             topic=topic, theme=theme, llm=llm)
            except Exception as e:
                print(
                    f"Error processing question {question_index} in batch {batch_index}: {str(e)}")
                continue

        if user_llm_messages_history and (len(user_llm_messages_history) >= (len(messages) * 2 - 10)):
            all_messages.append(user_llm_messages_history)

            with open(output_address, 'wb') as f:
                pickle.dump(all_messages, f)
        else:
            break

    with open(output_address, 'wb') as f:
        pickle.dump(all_messages, f)


def generate_probing_questions_candidate(plan_address: str,
                                         probing_question_type: str,
                                         llm_name: str,
                                         chat_address: str,
                                         save_address: str,
                                         file_name: str,
                                         domain: str):

    with open(plan_address, 'rb') as f:
        plans = pickle.load(f)

    original_plan = ""
    for plan_index, plan in enumerate(plans):
        current_plan = ""
        plan_bullets = extract_plan_bullets(plan)
        for bullet_index, bullet in enumerate(plan_bullets):
            current_plan += f"Bullet Number: {bullet_index+1} -> {bullet} \n"

        original_plan += f"BATCH {plan_index+1} PLAN \n" + \
            current_plan + "\n\n"

    if llm_name == "gpt":
        llm = gpt_llm
    elif llm_name == "qwen":
        llm = qwen_llm
    elif llm_name == "llama":
        llm = llama_llm

    if probing_question_type == "information_extraction":
        prompt = information_extraction_prompt\
            .replace("<plan>", original_plan)\
            .replace("<bullet_number>", "8-10")

    elif probing_question_type == "multi_session_reasoning":
        prompt = multi_session_reasoning_prompt.replace(
            "<plan>", original_plan)

    elif probing_question_type == "knowledge_update":
        prompt = knowledge_update_special_bullets_prompt.replace(
            "<plan>", original_plan)

    elif probing_question_type == "temporal_reasoning":
        prompt = temporal_reasoning_prompt.replace("<plan>", original_plan)

    elif probing_question_type == "preference_following":
        prompt = preference_following_prompt\
            .replace("<plan>", original_plan)\
            .replace("<bullet_number>", "8-12")

    elif probing_question_type == "event_ordering":
        prompt = event_ordering_prompt.replace(
            "<plan>", original_plan)

    elif probing_question_type == "contradiction_resolution":
        prompt = contradiction_resolution_prompt\
            .replace("<plan>", original_plan)\
            .replace("<bullet_number>", "8-12")

    elif probing_question_type == "summarization":
        prompt = summarization_prompt.replace("<plan>", original_plan)

    elif probing_question_type == "instruction_following":
        prompt = instruction_following_prompt.replace("<plan>", original_plan)

    response = llm.invoke(prompt).content
    data = json.loads(repair_json(response))

    probing_questions_directory = os.path.join(
        save_address, "probing_questions")
    if not os.path.isdir(probing_questions_directory):
        os.makedirs(probing_questions_directory, exist_ok=True)

    current_probing_question_directory = os.path.join(
        probing_questions_directory, probing_question_type)
    if not os.path.isdir(current_probing_question_directory):
        os.makedirs(current_probing_question_directory, exist_ok=True)

    qas_file = os.path.join(
        current_probing_question_directory, f"{file_name}.json")

    qas = []
    print(f"Number of questions: {len(data)}")
    for index, obj in enumerate(data):
        print(f"Question Num: {index}")
        batch_numbers = str(obj['batch_numbers'])
        bullet_numbers = str(obj['bullet_numbers'])
        indexes = []
        bullets = obj['bullet_points'].split("|")
        if len(batch_numbers.split(",")) == len(bullet_numbers.split(",")):
            for i, batch_number in enumerate(batch_numbers.split(",")):
                indexes.append(
                    [f"{str(batch_number)}", f"{str(bullet_numbers.split(',')[i])}"])
        else:
            for i, bullet_number in enumerate(bullet_numbers.split(",")):
                indexes.append([batch_numbers, str(bullet_number)])

        response = generate_probing_questions(chat_address=chat_address,
                                              indexes=indexes,
                                              bullets=bullets,
                                              probing_question_type=probing_question_type,
                                              llm_name=llm_name,
                                              domain=domain)

        qas.append(response)

        with open(qas_file, 'w') as f:
            json.dump(qas, f, indent=4)

    with open(qas_file, 'w') as f:
        json.dump(qas, f, indent=4)


def generate_probing_questions(chat_address: str,
                               indexes: list,
                               bullets: list,
                               probing_question_type: str,
                               llm_name: str,
                               domain: str = "general",
                               plan_address: str = None,
                               chat_length: str = None,
                               plan_number: str = None):

    def parse_json_response(response: str):
        """
        Parses a potentially malformed JSON string with multiple fallbacks.
        """
        s = response.strip()

        if s.startswith("```"):
            m = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", s)
            if m:
                s = m.group(1).strip()

        s = s.replace("“", '"').replace(
            "”", '"').replace("’", "'").replace("‘", "'")

        s = re.sub(r',(\s*[}\]])', r'\1', s)

        s = re.sub(r'([{\s,])(\w+?)\s*:', r'\1"\2":', s)

        try:
            return json.loads(s)
        except json.JSONDecodeError as e:
            try:
                s_python = s.replace('true', 'True').replace(
                    'false', 'False').replace('null', 'None')

                py_obj = ast.literal_eval(s_python)

                return json.loads(json.dumps(py_obj))
            except Exception:
                raise ValueError(f"Failed to parse JSON: {e}")

    def parse_with_repair_library(response: str) -> dict | list:
        """
        Parses a potentially malformed JSON string from an LLM using the
        json-repair library. This is the recommended approach.
        """
        try:
            return json.loads(repair_json(response))
        except Exception as e:
            print(e)
            with open("bad_json.log", "a", encoding="utf-8") as f:
                f.write(
                    f"---- FAILED WITH json-repair ----\n{response}\nError: {e}\n")
            raise ValueError(
                f"Failed to parse JSON even with repair library: {e}")

    def _get_token_encoder():
        """Initialize the best available token encoder"""
        try:
            import tiktoken
            encoders_to_try = ["cl100k_base", "p50k_base", "r50k_base"]

            for encoding_name in encoders_to_try:
                try:
                    encoder = tiktoken.get_encoding(encoding_name)
                    # print(f"Using tiktoken with {encoding_name} encoding")
                    return encoder
                except:
                    continue
        except:
            pass

    if llm_name == "gpt":
        llm = gpt_llm
    elif llm_name == "qwen":
        llm = qwen_llm
    elif llm_name == "llama":
        llm = llama_llm

    with open(chat_address, 'r') as file:
        data = json.load(file)

    if chat_length == "10M":
        data = data[plan_number][f"plan-{plan_number+1}"]

    selected_turns = []
    for index in indexes:
        batch_number = index[0].strip()
        bullet_number = index[1].strip()

        for i, obj in enumerate(data):
            if str(i+1) == batch_number:
                turns = obj["turns"]
                for turn in turns:
                    if turn[0]["index"].split(",")[1].strip() == bullet_number:
                        selected_turns.append(turn)

    chats = []
    for turn in selected_turns:
        chat_history = ""
        for message in turn:
            if message['role'] == 'user' or (message['role'] == 'assistant' and (probing_question_type == 'information_extraction' or
                                                                                 probing_question_type == 'multi_session_reasoning' or
                                                                                 probing_question_type == 'summarization')):
                if "id" in message.keys():
                    chat_history += f"chat_id: {message['id']}, {message['role'].upper()}: {message['content']} \n\n"
                else:
                    chat_history += f"{message['role'].upper()}: {message['content']} \n\n"

        chat_history += "\n\n"

        token_num = len(_get_token_encoder().encode(chat_history))
        max_tokens = 27000 // len(selected_turns)
        if token_num > max_tokens:
            prompt = f"""Summarize the following conversation in NO MORE than {max_tokens} tokens. 
                    Focus on key decisions, important information, and progress made. Be concise but preserve important context.
                    CRITICAL NOTE: When providing summary, include "chat_id: chat_id_number" for each turn you include in the summary.
                    CRITICAL NOTE: DO NOT COMBINE chat_ids together as far as you can like: chat_id: x-x+5
                    Conversation: {chat_history}
                    NOTE: keep under {max_tokens} tokens.
                    NOTE: Just provide the summary without any explanation before and after the summary."""

            chat_history = llm.invoke(prompt).content.strip()

        chats.append(chat_history)

    bullet_texts = "\n\n".join(bullets)
    chat_texts = "\n\n\n\n".join(chats)

    prompts = []
    if probing_question_type == "information_extraction":
        prompt = information_extraction_probing_question_easy_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

        prompt = information_extraction_probing_question_medium_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

        prompt = information_extraction_probing_question_hard_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

    elif probing_question_type == "multi_session_reasoning":
        prompt = multi_session_reasoning_probing_question_easy_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

        prompt = multi_session_reasoning_probing_question_medium_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

        prompt = multi_session_reasoning_probing_question_hard_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

    elif probing_question_type == "knowledge_update":
        prompt = knowledge_update_probing_question_final_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)

    elif probing_question_type == "temporal_reasoning":
        prompt = temporal_reasoning_probing_question_easy_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

        prompt = temporal_reasoning_probing_question_medium_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

        prompt = temporal_reasoning_probing_question_hard_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

    elif probing_question_type == "abstention":
        with open(plan_address, 'rb') as f:
            plans = pickle.load(f)

        original_plan = ""
        for plan_index, plan in enumerate(plans):
            current_plan = ""
            plan_bullets = extract_plan_bullets(plan)
            for bullet_index, bullet in enumerate(plan_bullets):
                current_plan += f"Bullet Number: {bullet_index+1} -> {bullet} \n"

            original_plan += f"BATCH {plan_index+1} PLAN \n" + \
                current_plan + "\n\n"

        prompt = abstention_probing_question_final_prompt\
            .replace("<plan>", original_plan)
        prompts.append(prompt)

    elif probing_question_type == "preference_following":
        prompt = preference_following_probing_question_final_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)

    elif probing_question_type == "event_ordering":
        prompt = event_ordering_probing_question_easy_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

        prompt = event_ordering_probing_question_medium_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

        prompt = event_ordering_probing_question_hard_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

    elif probing_question_type == "contradiction_resolution":
        prompt = contradiction_resolution_probing_question_final_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)

    elif probing_question_type == "summarization":
        prompt = summarization_probing_question_easy_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

        prompt = summarization_probing_question_medium_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

        prompt = summarization_probing_question_hard_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)

        prompts.append(prompt)

    elif probing_question_type == "instruction_following":
        prompt = instruction_following_probing_question_final_prompt\
            .replace("<bullet_point>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)

    datas = []

    for prompt in prompts:
        response = llm.invoke(prompt).content

        # data = parse_json_response(response=response)
        data = parse_with_repair_library(response=response)
        datas.append(data)

    return datas


def run_probing_question_parallel(plan_address: str,
                                  model: str,
                                  chat_address: str,
                                  save_directory: str,
                                  domain: str):

    question_types = ["information_extraction", "multi_session_reasoning", "knowledge_update",
                      "temporal_reasoning", "preference_following", "event_ordering",
                      "contradiction_resolution", "summarization", "instruction_following"]

    with ThreadPoolExecutor(max_workers=len(question_types)+1) as executor:
        futures = {
            executor.submit(
                generate_probing_questions_candidate,
                plan_address=plan_address,
                probing_question_type=q,
                llm_name=model,
                chat_address=chat_address,
                save_address=save_directory,
                file_name=q,
                domain=domain
            ): q
            for q in question_types
        }

        for future in as_completed(futures):
            qtype = futures[future]
            try:
                result = future.result()
                # print(f"[{qtype}] done")
            except Exception as e:
                print(f"[{qtype}] generated an exception: {e!r}")

    response = generate_probing_questions(chat_address=chat_address,
                                          indexes=[],
                                          bullets=[],
                                          probing_question_type="abstention",
                                          llm_name=model,
                                          plan_address=plan_address,
                                          domain=domain)

    abstention_save_address = os.path.join(
        save_directory, "probing_questions/abstention/abstention.json")
    os.makedirs(os.path.dirname(abstention_save_address), exist_ok=True)
    with open(abstention_save_address, 'w') as f:
        json.dump([response], f, indent=4)


def create_probing_questions(chats_directory: str,
                             start_index: int,
                             end_index: int,
                             model: str):

    entries = os.listdir(chats_directory)

    dirs = sorted(
        [name for name in entries if os.path.isdir(
            os.path.join(chats_directory, name))],
        key=lambda x: int(x)
    )

    dirs = dirs[start_index:end_index]

    max_workers = end_index - start_index
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for dir in dirs:
            if os.path.exists(os.path.join(chats_directory, dir, "plan_new_trunecated.pickle")):
                plan_address = os.path.join(
                    chats_directory, dir, "plan_new_trunecated.pickle")
            else:
                plan_address = os.path.join(
                    chats_directory, dir, "plan_new.pickle")
            if os.path.exists(os.path.join(chats_directory, dir, "chat_trunecated.json")):
                chat_address = os.path.join(
                    chats_directory, dir, "chat_trunecated.json")
            else:
                chat_address = os.path.join(chats_directory, dir, "chat.json")
            save_directory = os.path.join(chats_directory, dir)
            topic_address = os.path.join(chats_directory, dir, "topic.json")

            with open(topic_address, "r", encoding="utf-8") as f:
                data = json.load(f)

            category = data["category"].lower()
            if category == "math":
                domain = "math"
            elif category == "coding":
                domain = "coding"
            else:
                domain = "general"

            futures.append(
                executor.submit(
                    run_probing_question_parallel,
                    plan_address=plan_address,
                    model=model,
                    chat_address=chat_address,
                    save_directory=save_directory,
                    domain=domain
                )
            )

        for future in as_completed(futures):
            try:
                result = future.result()
                # print("Task finished:", result)
            except Exception as e:
                print("Task raised exception:", e)
