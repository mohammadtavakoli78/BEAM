import pickle
import json
import re
import os
from typing import List, Dict, Any
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
import numpy as np
import ast
from json_repair import repair_json

from llm import *
from prompts import *
from profile_creation import create_profile
from main import user_messages_generation, answer_generation, extract_plan_bullets, add_special_bullets_to_plan, generate_probing_questions, user_messages_generation_fast


def generate_labels(topic: str, 
                    theme: str, 
                    domain: str) -> list[str]:
    
    if domain == "general":
        prompt = label_generation_prompt_template.format(topic, theme)
    elif domain == "coding":
        prompt = coding_label_generation_prompt_template.format(topic, theme)
    elif domain == "math":
        prompt = math_label_generation_prompt_template.format(topic, theme)

    response = gpt_llm.invoke(prompt).content

    return response


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


def format_all_subtopic_plans(subtopic_data: Dict) -> str:
    """
    Format all subtopic plans into a structured string for prompt input.
    Args:
        subtopic_data: The JSON output from subtopic generation containing all 10 subtopics
    Returns:
        Formatted string containing all subtopic information
    """
    output = []
    output.append("=== ALL SUBTOPIC PLANS CONTEXT ===\n")
    output.append(f"MAIN TOPIC: {subtopic_data['main_topic']}")
    output.append(f"MAIN THEME: {subtopic_data['main_theme']}")
    output.append(
        f"MAIN SUBTOPICS: {', '.join(subtopic_data['main_subtopics'])}")
    output.append(f"TOTAL TIMELINE: {subtopic_data['total_timeline']}")
    output.append("")

    # Master Timeline Information
    master_timeline = subtopic_data.get('master_timeline', {})
    output.append("MASTER TIMELINE:")
    output.append(
        f"  Timeline Start: {master_timeline.get('timeline_start', 'N/A')}")
    output.append(
        f"  Timeline End: {master_timeline.get('timeline_end', 'N/A')}")
    output.append(
        f"  Main Action Starts: {master_timeline.get('main_action_starts', 'N/A')}")
    output.append(
        f"  Main Action Ends: {master_timeline.get('main_action_ends', 'N/A')}")
    output.append(
        f"  Main Action Duration: {master_timeline.get('main_action_duration', 'N/A')}")
    output.append("")

    # Phase Information
    output.append("PHASE BREAKDOWN:")
    for phase_name, phase_info in master_timeline.items():
        if isinstance(phase_info, dict) and 'start' in phase_info:
            output.append(f"  {phase_name.replace('_', ' ').title()}:")
            output.append(f"    Start: {phase_info['start']}")
            output.append(f"    End: {phase_info['end']}")
            if 'duration' in phase_info:
                output.append(f"    Duration: {phase_info['duration']}")
            output.append(f"    Topics: {phase_info['topics']}")
    output.append("")

    output.append("SUBTOPIC BREAKDOWN:")

    for subtopic in subtopic_data['subtopics']:
        output.append(f"\n--- SUBTOPIC {subtopic['id']} ---")
        output.append(f"Title: {subtopic['title']}")
        output.append(f"Theme: {subtopic['theme']}")
        output.append(f"Timeline: {subtopic['timeline']}")
        output.append(f"Phase Type: {subtopic['phase_type']}")
        output.append(f"Category: {subtopic['category']}")

        # Action Dates
        action_dates = subtopic.get('action_dates', {})
        output.append("Action Dates:")
        output.append(
            f"  Main Action Type: {action_dates.get('main_action_type', 'N/A')}")
        output.append(
            f"  Main Action Starts: {action_dates.get('main_action_starts', 'N/A')}")
        output.append(
            f"  Main Action Ends: {action_dates.get('main_action_ends', 'N/A')}")
        output.append(
            f"  Main Action Duration: {action_dates.get('main_action_duration', 'N/A')}")
        output.append(
            f"  Current Phase Relation: {action_dates.get('current_phase_relation', 'N/A')}")

        # Phase Boundaries
        phase_boundaries = subtopic.get('phase_boundaries', {})
        output.append("Phase Boundaries:")
        output.append(
            f"  Can Mention: {', '.join(phase_boundaries.get('can_mention', []))}")
        output.append(
            f"  Cannot Mention: {', '.join(phase_boundaries.get('cannot_mention', []))}")
        output.append(
            f"  Tense for Main Action: {phase_boundaries.get('tense_for_main_action', 'N/A')}")

        output.append("Sub-elements:")
        for i, sub_elem in enumerate(subtopic['subtopics'], 1):
            output.append(f"  {i}. {sub_elem}")

        output.append("Key Milestones:")
        for i, milestone in enumerate(subtopic['key_milestones'], 1):
            output.append(f"  {i}. {milestone}")

        output.append("Future References:")
        for i, ref in enumerate(subtopic['future_references'], 1):
            output.append(f"  {i}. {ref}")

        output.append("Continuity Hooks:")
        for i, hook in enumerate(subtopic.get('continuity_hooks', []), 1):
            output.append(f"  {i}. {hook}")

    output.append("\n" + "="*50 + "\n")

    return "\n".join(output)


def format_all_subtopic_plans_coding(subtopic_data: Dict) -> str:
    """
    Format all technical subtopic plans into a structured string for prompt input.
    Args:
        subtopic_data: The JSON output from technical subtopic generation containing all 5 subtopics
    Returns:
        Formatted string containing all technical subtopic information
    """
    output = []
    output.append("=== ALL TECHNICAL SUBTOPIC PLANS CONTEXT ===\n")
    output.append(f"MAIN TOPIC: {subtopic_data['main_topic']}")
    output.append(f"MAIN THEME: {subtopic_data['main_theme']}")
    output.append(
        f"MAIN SUBTOPICS: {', '.join(subtopic_data['main_subtopics'])}")
    output.append(f"TOTAL TIMELINE: {subtopic_data['total_timeline']}")
    output.append("")

    # Master Timeline Information
    master_timeline = subtopic_data.get('master_timeline', {})
    output.append("MASTER TECHNICAL TIMELINE:")
    output.append(
        f"  Timeline Start: {master_timeline.get('timeline_start', 'N/A')}")
    output.append(
        f"  Timeline End: {master_timeline.get('timeline_end', 'N/A')}")
    output.append(
        f"  Main Development Starts: {master_timeline.get('main_development_starts', 'N/A')}")
    output.append(
        f"  Main Development Ends: {master_timeline.get('main_development_ends', 'N/A')}")
    output.append(
        f"  Main Development Duration: {master_timeline.get('main_development_duration', 'N/A')}")
    output.append("")

    # Technical Phase Information
    output.append("TECHNICAL PHASE BREAKDOWN:")
    for phase_name, phase_info in master_timeline.items():
        if isinstance(phase_info, dict) and 'start' in phase_info:
            output.append(f"  {phase_name.replace('_', ' ').title()}:")
            output.append(f"    Start: {phase_info['start']}")
            output.append(f"    End: {phase_info['end']}")
            if 'duration' in phase_info:
                output.append(f"    Duration: {phase_info['duration']}")
            output.append(f"    Topics: {phase_info['topics']}")
    output.append("")

    output.append("TECHNICAL SUBTOPIC BREAKDOWN:")

    for subtopic in subtopic_data['subtopics']:
        output.append(f"\n--- TECHNICAL SUBTOPIC {subtopic['id']} ---")
        output.append(f"Title: {subtopic['title']}")
        output.append(f"Theme: {subtopic['theme']}")
        output.append(f"Timeline: {subtopic['timeline']}")
        output.append(f"Phase Type: {subtopic['phase_type']}")
        output.append(f"Category: {subtopic['category']}")

        # Development Dates
        development_dates = subtopic.get('development_dates', {})
        output.append("Development Dates:")
        output.append(
            f"  Main Development Type: {development_dates.get('main_development_type', 'N/A')}")
        output.append(
            f"  Main Development Starts: {development_dates.get('main_development_starts', 'N/A')}")
        output.append(
            f"  Main Development Ends: {development_dates.get('main_development_ends', 'N/A')}")
        output.append(
            f"  Main Development Duration: {development_dates.get('main_development_duration', 'N/A')}")
        output.append(
            f"  Current Phase Relation: {development_dates.get('current_phase_relation', 'N/A')}")

        # Technical Phase Boundaries
        phase_boundaries = subtopic.get('phase_boundaries', {})
        output.append("Technical Phase Boundaries:")
        output.append(
            f"  Can Mention: {', '.join(phase_boundaries.get('can_mention', []))}")
        output.append(
            f"  Cannot Mention: {', '.join(phase_boundaries.get('cannot_mention', []))}")
        output.append(
            f"  Tense for Main Development: {phase_boundaries.get('tense_for_main_development', 'N/A')}")

        output.append("Technical Sub-elements:")
        for i, sub_elem in enumerate(subtopic['subtopics'], 1):
            output.append(f"  {i}. {sub_elem}")

        output.append("Key Technical Milestones:")
        for i, milestone in enumerate(subtopic.get('key_technical_milestones', []), 1):
            output.append(f"  {i}. {milestone}")

        output.append("Future Technical References:")
        for i, ref in enumerate(subtopic.get('future_technical_references', []), 1):
            output.append(f"  {i}. {ref}")

        output.append("Technical Continuity Hooks:")
        for i, hook in enumerate(subtopic.get('technical_continuity_hooks', []), 1):
            output.append(f"  {i}. {hook}")

    output.append("\n" + "="*50 + "\n")

    return "\n".join(output)


def format_all_subtopic_plans_math(subtopic_data: Dict) -> str:
    """
    Format all mathematical subtopic plans into a structured string for prompt input.
    Args:
        subtopic_data: The JSON output from mathematical subtopic generation containing all 5 subtopics
    Returns:
        Formatted string containing all mathematical subtopic information
    """
    output = []
    output.append("=== ALL MATHEMATICAL SUBTOPIC PLANS CONTEXT ===\n")
    output.append(f"MAIN TOPIC: {subtopic_data['main_topic']}")
    output.append(f"MAIN THEME: {subtopic_data['main_theme']}")
    output.append(
        f"MAIN SUBTOPICS: {', '.join(subtopic_data['main_subtopics'])}")
    output.append(f"TOTAL TIMELINE: {subtopic_data['total_timeline']}")
    output.append("")

    # Master Timeline Information
    master_timeline = subtopic_data.get('master_timeline', {})
    output.append("MASTER MATHEMATICAL TIMELINE:")
    output.append(
        f"  Timeline Start: {master_timeline.get('timeline_start', 'N/A')}")
    output.append(
        f"  Timeline End: {master_timeline.get('timeline_end', 'N/A')}")
    output.append(
        f"  Main Study Starts: {master_timeline.get('main_study_starts', 'N/A')}")
    output.append(
        f"  Main Study Ends: {master_timeline.get('main_study_ends', 'N/A')}")
    output.append(
        f"  Main Study Duration: {master_timeline.get('main_study_duration', 'N/A')}")
    output.append("")

    # Mathematical Phase Information
    output.append("MATHEMATICAL PHASE BREAKDOWN:")
    for phase_name, phase_info in master_timeline.items():
        if isinstance(phase_info, dict) and 'start' in phase_info:
            output.append(f"  {phase_name.replace('_', ' ').title()}:")
            output.append(f"    Start: {phase_info['start']}")
            output.append(f"    End: {phase_info['end']}")
            if 'duration' in phase_info:
                output.append(f"    Duration: {phase_info['duration']}")
            output.append(f"    Topics: {phase_info['topics']}")
    output.append("")

    output.append("MATHEMATICAL SUBTOPIC BREAKDOWN:")

    for subtopic in subtopic_data['subtopics']:
        output.append(f"\n--- MATHEMATICAL SUBTOPIC {subtopic['id']} ---")
        output.append(f"Title: {subtopic['title']}")
        output.append(f"Theme: {subtopic['theme']}")
        output.append(f"Timeline: {subtopic['timeline']}")
        output.append(f"Phase Type: {subtopic['phase_type']}")
        output.append(f"Category: {subtopic['category']}")

        # Study Dates
        study_dates = subtopic.get('study_dates', {})
        output.append("Study Dates:")
        output.append(
            f"  Main Study Type: {study_dates.get('main_study_type', 'N/A')}")
        output.append(
            f"  Main Study Starts: {study_dates.get('main_study_starts', 'N/A')}")
        output.append(
            f"  Main Study Ends: {study_dates.get('main_study_ends', 'N/A')}")
        output.append(
            f"  Main Study Duration: {study_dates.get('main_study_duration', 'N/A')}")
        output.append(
            f"  Current Phase Relation: {study_dates.get('current_phase_relation', 'N/A')}")

        # Mathematical Phase Boundaries
        phase_boundaries = subtopic.get('phase_boundaries', {})
        output.append("Mathematical Phase Boundaries:")
        output.append(
            f"  Can Mention: {', '.join(phase_boundaries.get('can_mention', []))}")
        output.append(
            f"  Cannot Mention: {', '.join(phase_boundaries.get('cannot_mention', []))}")
        output.append(
            f"  Tense for Main Study: {phase_boundaries.get('tense_for_main_study', 'N/A')}")

        output.append("Mathematical Sub-elements:")
        for i, sub_elem in enumerate(subtopic['subtopics'], 1):
            output.append(f"  {i}. {sub_elem}")

        output.append("Key Mathematical Milestones:")
        for i, milestone in enumerate(subtopic.get('key_mathematical_milestones', []), 1):
            output.append(f"  {i}. {milestone}")

        output.append("Future Mathematical References:")
        for i, ref in enumerate(subtopic.get('future_mathematical_references', []), 1):
            output.append(f"  {i}. {ref}")

        output.append("Mathematical Continuity Hooks:")
        for i, hook in enumerate(subtopic.get('mathematical_continuity_hooks', []), 1):
            output.append(f"  {i}. {hook}")

    output.append("\n" + "="*50 + "\n")

    return "\n".join(output)


def format_current_subtopic_data(subtopic: Dict) -> str:
    """
    Format current subtopic data for use in plan generation prompt.
    Args:
        subtopic: A single subtopic dictionary from the subtopics array
    Returns:
        Formatted string containing current subtopic information
    """
    output = []
    output.append("=== CURRENT SUBTOPIC DATA ===\n")
    output.append(f"ID: {subtopic['id']}")
    output.append(f"Title: {subtopic['title']}")
    output.append(f"Theme: {subtopic['theme']}")
    output.append(f"Timeline: {subtopic['timeline']}")
    output.append(f"Phase Type: {subtopic['phase_type']}")
    output.append(f"Category: {subtopic['category']}")
    output.append("")

    # Action Dates (Critical for temporal boundaries)
    action_dates = subtopic.get('action_dates', {})
    output.append("ACTION DATES (CRITICAL):")
    output.append(
        f"  main_action_type: {action_dates.get('main_action_type', 'N/A')}")
    output.append(
        f"  main_action_starts: {action_dates.get('main_action_starts', 'N/A')}")
    output.append(
        f"  main_action_ends: {action_dates.get('main_action_ends', 'N/A')}")
    output.append(
        f"  main_action_duration: {action_dates.get('main_action_duration', 'N/A')}")
    output.append(
        f"  current_phase_relation: {action_dates.get('current_phase_relation', 'N/A')}")
    output.append("")

    # Phase Boundaries (Critical for content enforcement)
    phase_boundaries = subtopic.get('phase_boundaries', {})
    output.append("PHASE BOUNDARIES:")
    output.append(f"  Can Mention: {phase_boundaries.get('can_mention', [])}")
    output.append(
        f"  Cannot Mention: {phase_boundaries.get('cannot_mention', [])}")
    output.append(
        f"  Tense for Main Action: {phase_boundaries.get('tense_for_main_action', 'N/A')}")
    output.append("")

    # Sub-elements (Focus areas)
    output.append("SUB-ELEMENTS (Focus Areas):")
    for i, sub_elem in enumerate(subtopic['subtopics'], 1):
        output.append(f"  {i}. {sub_elem}")
    output.append("")

    # Key Milestones
    output.append("KEY MILESTONES:")
    for i, milestone in enumerate(subtopic['key_milestones'], 1):
        output.append(f"  {i}. {milestone}")
    output.append("")

    # Future References
    output.append("FUTURE REFERENCES:")
    for i, ref in enumerate(subtopic['future_references'], 1):
        output.append(f"  {i}. {ref}")
    output.append("")

    # Continuity Hooks
    output.append("CONTINUITY HOOKS:")
    for i, hook in enumerate(subtopic.get('continuity_hooks', []), 1):
        output.append(f"  {i}. {hook}")

    output.append("\n" + "="*50 + "\n")

    return "\n".join(output)


def format_current_subtopic_data_coding(subtopic: Dict) -> str:
    """
    Format current technical subtopic data for use in plan generation prompt.
    Args:
        subtopic: A single technical subtopic dictionary from the subtopics array
    Returns:
        Formatted string containing current technical subtopic information
    """
    output = []
    output.append("=== CURRENT TECHNICAL SUBTOPIC DATA ===\n")
    output.append(f"ID: {subtopic['id']}")
    output.append(f"Title: {subtopic['title']}")
    output.append(f"Theme: {subtopic['theme']}")
    output.append(f"Timeline: {subtopic['timeline']}")
    output.append(f"Phase Type: {subtopic['phase_type']}")
    output.append(f"Category: {subtopic['category']}")
    output.append("")

    # Development Dates (Critical for temporal boundaries)
    development_dates = subtopic.get('development_dates', {})
    output.append("DEVELOPMENT DATES (CRITICAL):")
    output.append(
        f"  main_development_type: {development_dates.get('main_development_type', 'N/A')}")
    output.append(
        f"  main_development_starts: {development_dates.get('main_development_starts', 'N/A')}")
    output.append(
        f"  main_development_ends: {development_dates.get('main_development_ends', 'N/A')}")
    output.append(
        f"  main_development_duration: {development_dates.get('main_development_duration', 'N/A')}")
    output.append(
        f"  current_phase_relation: {development_dates.get('current_phase_relation', 'N/A')}")
    output.append("")

    # Technical Phase Boundaries (Critical for content enforcement)
    phase_boundaries = subtopic.get('phase_boundaries', {})
    output.append("TECHNICAL PHASE BOUNDARIES:")
    output.append(f"  Can Mention: {phase_boundaries.get('can_mention', [])}")
    output.append(
        f"  Cannot Mention: {phase_boundaries.get('cannot_mention', [])}")
    output.append(
        f"  Tense for Main Development: {phase_boundaries.get('tense_for_main_development', 'N/A')}")
    output.append("")

    # Technical Sub-elements (Focus areas)
    output.append("TECHNICAL SUB-ELEMENTS (Focus Areas):")
    for i, sub_elem in enumerate(subtopic['subtopics'], 1):
        output.append(f"  {i}. {sub_elem}")
    output.append("")

    # Key Technical Milestones
    output.append("KEY TECHNICAL MILESTONES:")
    for i, milestone in enumerate(subtopic.get('key_technical_milestones', []), 1):
        output.append(f"  {i}. {milestone}")
    output.append("")

    # Future Technical References
    output.append("FUTURE TECHNICAL REFERENCES:")
    for i, ref in enumerate(subtopic.get('future_technical_references', []), 1):
        output.append(f"  {i}. {ref}")
    output.append("")

    # Technical Continuity Hooks
    output.append("TECHNICAL CONTINUITY HOOKS:")
    for i, hook in enumerate(subtopic.get('technical_continuity_hooks', []), 1):
        output.append(f"  {i}. {hook}")

    output.append("\n" + "="*50 + "\n")
    return "\n".join(output)


def format_current_subtopic_data_math(subtopic: Dict) -> str:
    """
    Format current mathematical subtopic data for use in plan generation prompt.
    Args:
        subtopic: A single mathematical subtopic dictionary from the subtopics array
    Returns:
        Formatted string containing current mathematical subtopic information
    """
    output = []
    output.append("=== CURRENT MATHEMATICAL SUBTOPIC DATA ===\n")
    output.append(f"ID: {subtopic['id']}")
    output.append(f"Title: {subtopic['title']}")
    output.append(f"Theme: {subtopic['theme']}")
    output.append(f"Timeline: {subtopic['timeline']}")
    output.append(f"Phase Type: {subtopic['phase_type']}")
    output.append(f"Category: {subtopic['category']}")
    output.append("")

    # Study Dates (Critical for temporal boundaries)
    study_dates = subtopic.get('study_dates', {})
    output.append("STUDY DATES (CRITICAL):")
    output.append(
        f"  main_study_type: {study_dates.get('main_study_type', 'N/A')}")
    output.append(
        f"  main_study_starts: {study_dates.get('main_study_starts', 'N/A')}")
    output.append(
        f"  main_study_ends: {study_dates.get('main_study_ends', 'N/A')}")
    output.append(
        f"  main_study_duration: {study_dates.get('main_study_duration', 'N/A')}")
    output.append(
        f"  current_phase_relation: {study_dates.get('current_phase_relation', 'N/A')}")
    output.append("")

    # Mathematical Phase Boundaries (Critical for content enforcement)
    phase_boundaries = subtopic.get('phase_boundaries', {})
    output.append("MATHEMATICAL PHASE BOUNDARIES:")
    output.append(f"  Can Mention: {phase_boundaries.get('can_mention', [])}")
    output.append(
        f"  Cannot Mention: {phase_boundaries.get('cannot_mention', [])}")
    output.append(
        f"  Tense for Main Study: {phase_boundaries.get('tense_for_main_study', 'N/A')}")
    output.append("")

    # Mathematical Sub-elements (Focus areas)
    output.append("MATHEMATICAL SUB-ELEMENTS (Focus Areas):")
    for i, sub_elem in enumerate(subtopic['subtopics'], 1):
        output.append(f"  {i}. {sub_elem}")
    output.append("")

    # Key Mathematical Milestones
    output.append("KEY MATHEMATICAL MILESTONES:")
    for i, milestone in enumerate(subtopic.get('key_mathematical_milestones', []), 1):
        output.append(f"  {i}. {milestone}")
    output.append("")

    # Future Mathematical References
    output.append("FUTURE MATHEMATICAL REFERENCES:")
    for i, ref in enumerate(subtopic.get('future_mathematical_references', []), 1):
        output.append(f"  {i}. {ref}")
    output.append("")

    # Mathematical Continuity Hooks
    output.append("MATHEMATICAL CONTINUITY HOOKS:")
    for i, hook in enumerate(subtopic.get('mathematical_continuity_hooks', []), 1):
        output.append(f"  {i}. {hook}")

    output.append("\n" + "="*50 + "\n")
    return "\n".join(output)


def summarize_previous_plans_with_llm(generated_plans: List[Dict], 
                                      subtopic_data: Dict, 
                                      current_subtopic_id: int, 
                                      llm) -> str:
    """
    Generate a concise summary of all previous plans using an LLM.

    Args:
        generated_plans: List of generated plans up to current point
        subtopic_data: The subtopic structure data
        current_subtopic_id: The ID of the current subtopic being generated
        llm_function: Function that takes a prompt and returns LLM response

    Returns:
        LLM-generated summary string of previous plans
    """

    if not generated_plans or current_subtopic_id == 0:
        return "No previous plans to summarize - this is the first subtopic."

    previous_plans = [
        plan for index, plan in enumerate(generated_plans) if index < current_subtopic_id]

    if not previous_plans:
        return "No previous plans available for summarization."

    plans_summarization_prompt = f"""You are a narrative continuity specialist. Analyze the provided plans and create a concise summary that preserves critical facts for story consistency.
    MAIN TOPIC: {subtopic_data['main_topic']}
    MAIN THEME: {subtopic_data['main_theme']}
    CURRENT SUBTOPIC: {current_subtopic_id}

    PREVIOUS PLANS TO SUMMARIZE:
    """

    for index, plan in enumerate(previous_plans):
        subtopic_info = next(
            (st for st in subtopic_data['subtopics'] if st['id'] == index), None)
        if subtopic_info:
            plans_summarization_prompt += f"\n--- SUBTOPIC {index}: {subtopic_info['title']} ---\n"
            plans_summarization_prompt += f"Timeline: {subtopic_info['timeline']}\n"
            plans_summarization_prompt += f"Plan Content:\n{plan[0]}\n"

    plans_summarization_prompt += f"""
    SUMMARIZATION REQUIREMENTS:
    Create a concise summary that includes ONLY the most critical information for maintaining story continuity:

    1. **CHARACTER FACTS**: Established details (age, job, salary, location, key personality traits)
    2. **TIMELINE ANCHORS**: Specific dates, deadlines, and scheduled events that future plans must honor
    3. **RELATIONSHIPS**: Core relationships and new people introduced with their roles
    4. **COMMITMENTS**: Financial decisions, bookings, promises, and obligations made
    5. **DECISIONS**: Key choices that affect future subtopics
    6. **FUTURE OBLIGATIONS**: Events/actions planned for upcoming subtopics

    FORMAT: Use clear sections with bullet points. Focus on FACTS that must remain consistent, not narrative descriptions.

    CRITICAL: Only include information that future plans MUST reference or could contradict. Exclude general narrative or emotional content.

    CRITICAL: Generate your summary in {len(previous_plans) * 100} words.
    Generate the summary now:"""

    try:
        summary = llm.invoke(plans_summarization_prompt).content
        return f"=== LLM-GENERATED PREVIOUS PLANS SUMMARY ===\n\n{summary}\n\n" + "="*50 + "\n"
    except Exception as e:
        return "N/A"


def ten_m_plan_generation(initial_topic: object, 
                          first_timeline: str, 
                          num_plans: int, 
                          num_batches: str, 
                          domain: str,
                          save_address: str, 
                          llm_name: str, 
                          mode: str):

    main_spec, relationships = create_profile(
        all_profile_size=300, friends_size=30, acquaintances_size=30)

    with open(f'{save_address}/main_spec.pickle', 'wb') as f:
        pickle.dump(main_spec, f)

    main_spec = format_user_profile_for_llm(main_spec=main_spec)

    with open(f'{save_address}/main_spec.txt', 'w', encoding='utf-8') as f:
        f.writelines(main_spec)

    SEED_TOPIC = initial_topic["title"]
    SEED_THEME = initial_topic["theme"]
    SEED_SUBTOPICS = initial_topic["subtopics"]
    USER_PROFILE = main_spec
    USER_RELATIONSHIPS = relationships
    TIMELINE = first_timeline

    if mode == "following":
        if domain == "general":
            if num_plans == 5:
                prompt_template = ten_m_generate_following_topics_five_plan
            elif num_plans == 10:
                prompt_template = ten_m_generate_following_topics
        elif domain == "coding":
            if num_plans == 5:
                prompt_template = ten_m_generate_following_topics_five_plan_coding
            elif num_plans == 10:
                prompt_template = ten_m_generate_following_topics_ten_plan_coding
        elif domain == "math":
            if num_plans == 5:
                prompt_template = ten_m_generate_following_topics_five_plan_math
            elif num_plans == 10:
                prompt_template = ten_m_generate_following_topics_ten_plan_math

        prompt = prompt_template.\
            replace("<seed_topic>", SEED_TOPIC).\
            replace("<seed_theme>", SEED_THEME).\
            replace("<seed_subtopics>", ", ".join(SEED_SUBTOPICS)).\
            replace("<user_profile>", USER_PROFILE).\
            replace("<timeline>", TIMELINE)

    elif mode == "similar":
        if domain == "general":
            if num_plans == 5:
                prompt_template = ten_m_generate_similar_topics_five_plan
            elif num_plans == 10:
                prompt_template = ten_m_generate_similar_topics
        elif domain == "coding":
            if num_plans == 5:
                prompt_template = ten_m_generate_similar_topics_five_plan_coding
            elif num_plans == 10:
                prompt_template = ten_m_generate_similar_topics_ten_plan_coding
        elif domain == "math":
            if num_plans == 5:
                prompt_template = ten_m_generate_similar_topics_five_plan_math
            elif num_plans == 10:
                prompt_template = ten_m_generate_similar_topics_ten_plan_math

        prompt = prompt_template.\
            replace("<main_topic>", SEED_TOPIC).\
            replace("<main_theme>", SEED_THEME).\
            replace("<main_subtopics>", ", ".join(SEED_SUBTOPICS)).\
            replace("<user_profile>", USER_PROFILE).\
            replace("<total_timeline>", TIMELINE)

    topic_response = gpt_llm.invoke(prompt).content

    clean = topic_response.strip('`').strip()
    if clean.startswith('json'):
        clean = clean[4:].strip()

    if mode == "following":
        topics = json.loads(clean)['topics']
    elif mode == "similar":
        clean = bytes(clean, "utf-8").decode("unicode_escape")
        parsed_subtopics = json.loads(clean)
        if domain == "general":
            formated_subtopics = format_all_subtopic_plans(
                subtopic_data=parsed_subtopics)
        elif domain == "coding":
            formated_subtopics = format_all_subtopic_plans_coding(
                subtopic_data=parsed_subtopics)
        elif domain == "math":
            formated_subtopics = format_all_subtopic_plans_math(
                subtopic_data=parsed_subtopics)

        topics = parsed_subtopics['subtopics']

    all_friends = relationships['friends']
    all_acquaintances = relationships['acquaintances']

    if llm_name == "gpt":
        gpt_llm_obj_temp = BuildLLm(model_url=None,
                       model_name="gpt-4.1-mini",
                       api_key=cfg["gpt"]["api_key"],
                       temperature=0.3)
        gpt_llm_temp = gpt_llm_obj_temp.build_llm()
    
        llm = gpt_llm_temp
    elif llm_name == "qwen":
        llm = qwen_llm
    elif llm_name == "llama":
        llm = llama_llm

    temp_core_relationships = relationships.copy()
    del temp_core_relationships['friends']
    del temp_core_relationships['acquaintances']

    with open(f'{save_address}/core_relationships.pickle', 'wb') as f:
        pickle.dump(temp_core_relationships, f)

    temp_core_relationships = format_relationships_for_llm(
        relationships=temp_core_relationships)

    with open(f'{save_address}/core_relationships.txt', 'w', encoding='utf-8') as f:
        f.writelines(temp_core_relationships)

    plans = []
    for index, item in enumerate(topics):
        print(f"Index: {index}")

        folder_path = os.path.join(save_address, f"plan-{str(index)}")
        os.makedirs(folder_path, exist_ok=True)

        with open(f'{save_address}/plan-{index}/topic.json', 'w', encoding='utf-8') as f:
            json.dump(item, f, indent=4)

        topic = item["title"]
        theme = item["theme"]
        subtopics = item["subtopics"]
        timeline = item["timeline"]

        labels = generate_labels(topic=topic, theme=theme, domain=domain)

        with open(f'{save_address}/plan-{index}/labels.txt', 'w', encoding='utf-8') as f:
            f.writelines(labels)

        friend_batches = np.array_split(all_friends, 10)
        acquaintance_batches = np.array_split(all_acquaintances, 10)

        friends = friend_batches[index].tolist()
        acquaintances = acquaintance_batches[index].tolist()

        temp_new_relationships = relationships.copy()
        if 'children' in temp_new_relationships.keys():
            del temp_new_relationships['children']
        if 'partner' in temp_new_relationships.keys():
            del temp_new_relationships['partner']
        if 'parent' in temp_new_relationships.keys():
            del temp_new_relationships['parent']

        temp_new_relationships['friends'] = friends
        temp_new_relationships['acquaintances'] = acquaintances

        with open(f'{save_address}/plan-{index}/new_relationships.json', 'w', encoding='utf-8') as f:
            json.dump(temp_new_relationships, f, indent=4)
        temp_new_relationships = format_relationships_for_llm(
            relationships=temp_new_relationships)
        with open(f'{save_address}/plan-{index}/new_relationships.txt', 'w', encoding='utf-8') as f:
            f.writelines(temp_new_relationships)

        previous_plan = "N/A" if index == 0 else plans[index - 1][0]
        is_first = "<YES>" if index == 0 else "<NO>"

        if mode == "following":
            if domain == "general":
                prompt_template = ten_m_following_plan_generation_prompt
            elif domain == "coding":
                prompt_template = ten_m_following_plan_generation_prompt_coding
            elif domain == "math":
                prompt_template = ten_m_following_plan_generation_prompt_math

            plan_generation_prompt = prompt_template.\
                replace("<topic>", topic).\
                replace("<theme>", theme + " -> " + ", ".join(subtopics)).\
                replace("<timeline>", timeline).\
                replace("<num_batches>", num_batches).\
                replace("<provided_labels>", labels).\
                replace("<user_profile>", main_spec).\
                replace("<core_relationships>", temp_core_relationships).\
                replace("<new_relationships>", temp_new_relationships).\
                replace("<previous_plan>", previous_plan).\
                replace("<YES/NO>", is_first)

        elif mode == "similar":
            if domain == "general":
                current_subtopic_data = format_current_subtopic_data(
                    subtopic=item)
            elif domain == "coding":
                current_subtopic_data = format_current_subtopic_data_coding(
                    subtopic=item)
            elif domain == "math":
                current_subtopic_data = format_current_subtopic_data_math(
                    subtopic=item)

            previous_plans_summary = summarize_previous_plans_with_llm(generated_plans=plans, subtopic_data=parsed_subtopics,
                                                                       current_subtopic_id=index, llm=llm)

            if domain == "general":
                prompt_template = ten_m_similar_plan_generation_prompt
            elif domain == "coding":
                prompt_template = ten_m_similar_plan_generation_prompt_coding
            elif domain == "math":
                prompt_template = ten_m_similar_plan_generation_prompt_math

            plan_generation_prompt = prompt_template.\
                replace("<main_topic>", SEED_TOPIC).\
                replace("<main_theme>", SEED_THEME + " -> " + ", ".join(SEED_SUBTOPICS)).\
                replace("<topic>", topic).\
                replace("<theme>", theme + " -> " + ", ".join(subtopics)).\
                replace("<timeline>", timeline).\
                replace("<num_batches>", num_batches).\
                replace("<provided_labels>", labels).\
                replace("<user_profile>", main_spec).\
                replace("<core_relationships>", temp_core_relationships).\
                replace("<new_relationships>", temp_new_relationships).\
                replace("<all_subtopic_plans>", formated_subtopics).\
                replace("<previous_plans_summary>", previous_plans_summary).\
                replace("<previous_plan>", previous_plan).\
                replace("<current_subtopic_data>", current_subtopic_data).\
                replace("<current_subtopic_id>", str(index)).\
                replace("<YES/NO>", is_first)

        plan_response = gpt_llm.invoke(plan_generation_prompt).content

        raw_batches = re.split(r'(BATCH \d+ PLAN)', plan_response)

        new_plans = []
        for i in range(1, len(raw_batches), 2):
            header = raw_batches[i].strip()
            content = raw_batches[i + 1].strip()
            new_plans.append(f"{header}\n{content}")

        with open(f'{save_address}/plan-{index}/plan.pickle', 'wb') as f:
            pickle.dump(new_plans, f)
        with open(f'{save_address}/plan-{index}/plan.txt', 'w', encoding='utf-8') as f:
            f.writelines(plan_response)

        plans.append([plan_response])


def ten_m_user_messages_generation(plan_save_address: str,
                                   num_batches: int,
                                   sub_batches_per_batch: int,
                                   sub_batch_size: int,
                                   batch_size: int,
                                   llm_name: str,
                                   domain: str,
                                   mode: str):

    if mode == "parallel":
        entries = os.listdir(plan_save_address)
        dirs = sorted([name for name in entries
                       if os.path.isdir(os.path.join(plan_save_address, name))])

        def _process_dir(dir_name: str):
            plan_path = os.path.join(
                plan_save_address, dir_name, "plan_new.pickle")
            topic_path = os.path.join(
                plan_save_address, dir_name, "topic.json")

            with open(plan_path, "rb") as f:
                plans = pickle.load(f)

            with open(topic_path, "r") as f:
                topic_data = json.load(f)

            topic = topic_data["category"] + " -> " + topic_data["title"]
            theme = (
                topic_data["theme"]
                + " -> "
                + ", ".join(topic_data["subtopics"])
            )

            user_messages_generation_fast(
                topic=topic,
                theme=theme,
                plans=plans,
                num_batches=num_batches,
                sub_batches_per_batch=sub_batches_per_batch,
                sub_batch_size=sub_batch_size,
                batch_size=batch_size,
                llm_name=llm_name,
                save_address=os.path.join(
                    plan_save_address, dir_name, f"user_messages.pickle"),
                domain=domain,
                sepcial_bullets=True
            )

        with ThreadPoolExecutor(max_workers=len(dirs)) as executor:

            futures = {executor.submit(_process_dir, d): d for d in dirs}

            for future in as_completed(futures):
                d = futures[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"[{d}] generated an exception: {e}")

    elif mode == "sequential":
        entries = os.listdir(plan_save_address)
        dirs = sorted([name for name in entries if os.path.isdir(
            os.path.join(plan_save_address, name))])

        for dir in dirs:
            plan_address = os.path.join(
                plan_save_address, dir, "plan_new.pickle")
            with open(plan_address, 'rb') as f:
                plans = pickle.load(f)

            topic_address = os.path.join(plan_save_address, dir, "topic.json")
            with open(topic_address, 'r') as f:
                topic_data = json.load(f)

            topic = topic_data["category"] + " -> " + topic_data["title"]
            theme = topic_data["theme"] + " -> " + \
                ", ".join(topic_data["subtopics"])

            save_address = os.path.join(
                plan_save_address, dir, f"user_messages.pickle")
            user_messages_generation_fast(topic=topic, theme=theme, plans=plans, num_batches=num_batches,
                                          sub_batches_per_batch=sub_batches_per_batch, sub_batch_size=sub_batch_size, batch_size=batch_size,
                                          llm_name=llm_name, save_address=save_address, domain=domain)


def ten_m_answer_generation(input_directory: str,
                            mode: str,
                            llm):

    entries = os.listdir(input_directory)
    dirs = dirs = sorted([
        name for name in entries
        if os.path.isdir(os.path.join(input_directory, name))
    ])

    def summarize_previous_plans(index: int):
        plans = []
        plans_summary = ""
        for i, dir in enumerate(dirs):
            if i < index:
                plan_address = os.path.join(
                    input_directory, dir, "plan_new.pickle")
                with open(plan_address, 'rb') as f:
                    plan = pickle.load(f)
                    plans.append(plan)

        for plan in plans:
            prompt = f"""Extract and summarize the most critical elements from the following plan in maximum 300 tokens.
                Explain main topic, key decisions, important names, and essential timelines.
                Plan: {plan}
                Format: ONLY output summary without extra explanation.
                Summary:"""

            summary = llm.invoke(prompt).content
            plans_summary += summary + "\n\n"

        return plans_summary

    if mode == "parallel":

        def _process_dir(index: int, dir_name: str):
            previous_plans_summary = summarize_previous_plans(index=index)

            plan_address = os.path.join(
                input_directory, dir_name, "plan_new.pickle")

            user_questions_address = os.path.join(
                input_directory, dir_name, f"user_messages.pickle")

            topic_address = os.path.join(
                input_directory, dir_name, "topic.json")
            with open(topic_address, 'r') as f:
                topic_data = json.load(f)

            topic = topic_data["category"] + " -> " + topic_data["title"]
            theme = topic_data["theme"] + " -> " + \
                ", ".join(topic_data["subtopics"])

            save_address = os.path.join(
                input_directory, dir_name, f"chat.pickle")

            answer_generation(input_address=user_questions_address, output_address=save_address, plans_address=plan_address,
                              topic=topic, theme=theme, llm=llm, previous_plans_summary=previous_plans_summary)

        with ThreadPoolExecutor(max_workers=len(dirs)) as executor:

            futures = {executor.submit(
                _process_dir, i, d): d for i, d in enumerate(dirs)}

            for future in as_completed(futures):
                d = futures[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"[{d}] generated an exception: {e}")

    elif mode == "sequential":

        for index, dir in enumerate(dirs):
            previous_plans_summary = summarize_previous_plans(index=index)

            plan_address = os.path.join(
                input_directory, dir, "plan_new.pickle")

            user_questions_address = os.path.join(
                input_directory, dir, f"user_messages.pickle")

            topic_address = os.path.join(input_directory, dir, "topic.json")
            with open(topic_address, 'r') as f:
                topic_data = json.load(f)

            topic = topic_data["category"] + " -> " + topic_data["title"]
            theme = topic_data["theme"] + " -> " + \
                ", ".join(topic_data["subtopics"])

            save_address = os.path.join(
                input_directory, dir, f"chat.pickle")

            answer_generation(input_address=user_questions_address, output_address=save_address, plans_address=plan_address,
                              topic=topic, theme=theme, llm=llm, previous_plans_summary=previous_plans_summary)


def ten_m_generate_probing_questions_candidate(chats_directory: str,
                                               probing_question_type: str,
                                               llm_name: str):

    def parse_json_response(response: str):
        s = response.strip()

        if s.startswith("```"):
            m = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", s)
            if m:
                s = m.group(1).strip()

        if (s.startswith("'") and s.endswith("'")) or (s.startswith('"') and s.endswith('"')):
            try:
                s = ast.literal_eval(s)
            except Exception:
                pass

        s = re.sub(r',(\s*[}\]])', r'\1', s)

        s = s.replace("“", '"').replace(
            "”", '"').replace("’", "'").replace("‘", "'")

        try:
            return json.loads(s)
        except json.JSONDecodeError as e:
            try:
                obj = ast.literal_eval(s)
                return json.loads(json.dumps(obj))
            except Exception:
                raise ValueError(f"Failed to parse JSON: {e}")

    def group_by_three_with_overlap(a):
        result = []
        for i in range(0, len(a), 2):
            group = a[i:i+2]
            if len(group) == 2:
                result.append(group)
            elif len(group) < 2 and len(result) > 0:
                last = result[-1]
                needed = 2 - len(group)
                new_group = last[-needed:] + group
                result.append(new_group)
        return result

    if llm_name == "gpt":
        llm = gpt_llm
    elif llm_name == "qwen":
        llm = qwen_llm
    elif llm_name == "llama":
        llm = llama_llm

    dirs = sorted([
        name for name in os.listdir(chats_directory)
        if (os.path.isdir(os.path.join(chats_directory, name)) and ('plan' in name))
    ])

    if probing_question_type in ["contradiction_resolution", "information_extraction",
                                 "instruction_following", "knowledge_update", "preference_following"]:

        plan_cutoff_address = os.path.join(chats_directory, "plan_cutoff.txt")
        with open(plan_cutoff_address, "r") as f:
            plan_cutoff = f.read().strip()
        plan_cutoff = int(plan_cutoff)

        dirs = dirs[:plan_cutoff]

        for dir_index, dir in enumerate(dirs):
            if os.path.exists(os.path.join(chats_directory, dir, "plan_new_trunecated.pickle")):
                plan_address = os.path.join(
                    chats_directory, dir, "plan_new_trunecated.pickle")
            else:
                plan_address = os.path.join(
                    chats_directory, dir, "plan_new.pickle")

            with open(plan_address, 'rb') as f:
                plan = pickle.load(f)

            original_plan = ""
            for plan_index, plan in enumerate(plan):
                current_plan = ""
                plan_bullets = extract_plan_bullets(plan)
                for bullet_index, bullet in enumerate(plan_bullets):
                    current_plan += f"Bullet Number: {bullet_index+1} -> {bullet} \n"

                original_plan += f"BATCH {plan_index+1} PLAN \n" + \
                    current_plan + "\n\n"

            if probing_question_type == "information_extraction":
                prompt = information_extraction_prompt\
                    .replace("<plan>", original_plan)\
                    .replace("<bullet_number>", "2")

            elif probing_question_type == "knowledge_update":
                prompt = knowledge_update_special_bullets_prompt.replace(
                    "<plan>", original_plan)

            elif probing_question_type == "preference_following":
                prompt = ten_m_preference_following_prompt\
                    .replace("<plan>", original_plan)\
                    .replace("<bullet_number>", "2")

            elif probing_question_type == "contradiction_resolution":
                prompt = contradiction_resolution_prompt\
                    .replace("<plan>", original_plan)\
                    .replace("<bullet_number>", "2")

            elif probing_question_type == "instruction_following":
                prompt = instruction_following_prompt.replace(
                    "<plan>", original_plan)

            response = llm.invoke(prompt).content
            data = json.loads(repair_json(response))

            probing_questions_directory = os.path.join(
                chats_directory, "probing_questions", f"plan_{dir_index}")
            if not os.path.isdir(probing_questions_directory):
                os.makedirs(probing_questions_directory, exist_ok=True)

            current_probing_question_directory = os.path.join(
                probing_questions_directory, probing_question_type)
            if not os.path.isdir(current_probing_question_directory):
                os.makedirs(current_probing_question_directory, exist_ok=True)

            qas_file = os.path.join(
                current_probing_question_directory, f"{probing_question_type}.json")

            if not os.path.isfile(qas_file):
                with open(qas_file, "w", encoding="utf-8") as f:
                    json.dump([], f, indent=4)

            qas = []
            with open(qas_file, "r", encoding="utf-8") as f:
                qas = json.load(f)

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

                if os.path.exists(os.path.join(chats_directory, "chat_trunecated.json")):
                    chat_address = os.path.join(
                        chats_directory, "chat_trunecated.json")
                else:
                    chat_address = os.path.join(chats_directory, "chat.json")

                response = generate_probing_questions(chat_address=chat_address,
                                                      indexes=indexes,
                                                      bullets=bullets,
                                                      probing_question_type=probing_question_type,
                                                      llm_name=llm_name,
                                                      plan_address=plan_address,
                                                      chat_length="10M",
                                                      plan_number=dir_index)

                qas.append(response)

                with open(qas_file, 'w') as f:
                    json.dump(qas, f, indent=4)

            with open(qas_file, 'w') as f:
                json.dump(qas, f, indent=4)

    else:
        plan_cutoff_address = os.path.join(chats_directory, "plan_cutoff.txt")
        with open(plan_cutoff_address, "r") as f:
            plan_cutoff = f.read().strip()
        plan_cutoff = int(plan_cutoff)

        dirs = dirs[:plan_cutoff]
        group_dirs = group_by_three_with_overlap(dirs)

        for group in group_dirs:
            base_plan_number = int(group[0].split("-")[1])
            combined_plan = ""
            for plan_index, dir in enumerate(group):
                if os.path.exists(os.path.join(chats_directory, dir, "plan_new_trunecated.pickle")):
                    plan_address = os.path.join(
                        chats_directory, dir, "plan_new_trunecated.pickle")
                else:
                    plan_address = os.path.join(
                        chats_directory, dir, "plan_new.pickle")

                with open(plan_address, 'rb') as f:
                    plan = pickle.load(f)

                current_plan = ""
                for batch_index, batch in enumerate(plan):
                    current_batch = ""
                    batch_bullets = extract_plan_bullets(batch)
                    for bullet_index, bullet in enumerate(batch_bullets):
                        current_batch += f"Bullet Number: {bullet_index+1} -> {bullet} \n"

                    current_plan += f"BATCH {batch_index+1} PLAN {base_plan_number + plan_index+1} \n" + \
                        current_batch + "\n\n"

                combined_plan += f"PLAN {base_plan_number + plan_index+1} \n\n" + \
                    current_plan + "\n\n\n\n"

            if probing_question_type == "multi_session_reasoning":
                prompt = ten_m_multi_session_reasoning_prompt_detailed.replace(
                    "<plans>", combined_plan)

            elif probing_question_type == "temporal_reasoning":
                prompt = ten_m_temporal_reasoning_prompt.replace(
                    "<plans>", combined_plan)

            elif probing_question_type == "event_ordering":
                prompt = ten_m_event_ordering_prompt_detailed.replace(
                    "<plans>", combined_plan)

            elif probing_question_type == "summarization":
                prompt = ten_m_summarization_prompt.replace(
                    "<plans>", combined_plan)

            with open('text.txt', 'w', encoding='utf-8') as f:
                f.writelines(prompt)

            response = llm.invoke(prompt).content
            
            try:
                data = parse_json_response(response=response)
            except Exception as e:
                print(f"Error in candidate generation {e}")
                data = json.loads(repair_json(response))

            first_plan_index = int(group[0].split("-")[1])
            last_plan_index = int(group[-1].split("-")[1])
            probing_questions_directory = os.path.join(
                chats_directory, "probing_questions", f"plan_{first_plan_index}-{last_plan_index}")
            if not os.path.isdir(probing_questions_directory):
                os.makedirs(probing_questions_directory, exist_ok=True)

            current_probing_question_directory = os.path.join(
                probing_questions_directory, probing_question_type)
            if not os.path.isdir(current_probing_question_directory):
                os.makedirs(current_probing_question_directory, exist_ok=True)

            qas_file = os.path.join(
                current_probing_question_directory, f"{probing_question_type}.json")

            if not os.path.isfile(qas_file):
                with open(qas_file, "w", encoding="utf-8") as f:
                    json.dump([], f, indent=4)

            qas = []
            with open(qas_file, "r", encoding="utf-8") as f:
                qas = json.load(f)
            print(f"Number of questions: {len(data)}")
            for index, obj in enumerate(data):
                print(f"Question Num: {index}")
                index = obj["index"]
                indexes = []
                for key in index.keys():
                    plan_number = int(key.split(" ")[1])
                    values = index[key]
                    for value in values:
                        batch_number = value[0]
                        bullet_number = value[1]
                        indexes.append(
                            [plan_number, batch_number, bullet_number])

                bullets = obj['bullet_points'].split("|")

                response = ten_m_generate_probing_questions(chats_directory=chats_directory,
                                                            group_address=group,
                                                            indexes=indexes,
                                                            bullets=bullets,
                                                            probing_question_type=probing_question_type,
                                                            llm_name=llm_name)

                qas.append(response)

                with open(qas_file, 'w') as f:
                    json.dump(qas, f, indent=4)

            with open(qas_file, 'w') as f:
                json.dump(qas, f, indent=4)


def ten_m_generate_probing_questions(chats_directory: str,
                                     group_address: str,
                                     indexes: list,
                                     bullets: list,
                                     probing_question_type: str,
                                     llm_name: str):

    chats = []

    if os.path.exists(os.path.join(chats_directory, "chat_trunecated.json")):
        chat_directory = os.path.join(chats_directory, "chat_trunecated.json")
    else:
        chat_directory = os.path.join(chats_directory, "chat.json")

    with open(chat_directory, 'r') as f:
        chat = json.load(f)

    def parse_json_response(response: str):
        response = response.strip()

        if response.startswith("```"):
            match = re.search(
                r"```(?:json)?\s*(\{.*\})\s*```", response, re.DOTALL)
            if match:
                response = match.group(1)

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            try:
                unescaped = bytes(response, "utf-8").decode("unicode_escape")
                return json.loads(unescaped)
            except Exception as e:
                raise ValueError(f"Failed to parse JSON after unescaping: {e}")

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

    first_plan_number = int(group_address[0].split('-')[1]) + 1
    second_plan_number = int(group_address[1].split('-')[1]) + 1

    chats.append(chat[first_plan_number-1][f'plan-{first_plan_number}'])
    chats.append(chat[second_plan_number-1][f'plan-{second_plan_number}'])

    selected_turns = {}
    len_selected_turns = 0
    for index in indexes:
        plan_number = index[0]
        batch_number = index[1]
        bullet_number = index[2]

        for i, obj in enumerate(chats[plan_number - first_plan_number]):
            if i+1 == batch_number:
                turns = obj["turns"]
                for turn in turns:
                    if turn[0]["index"].split(",")[1] != 'N/A':
                        if turn[0]["index"].split(",")[1].isdigit():
                            if int(turn[0]["index"].split(",")[1]) == bullet_number:
                                if plan_number in selected_turns.keys():
                                    temp = selected_turns[plan_number]
                                    temp.append(turn)
                                    selected_turns[plan_number] = temp
                                    len_selected_turns += 1
                                else:
                                    selected_turns[plan_number] = [turn]
                                    len_selected_turns += 1

    chats = []
    for key in selected_turns.keys():
        for turn in selected_turns[key]:
            chat_history = ""
            for message in turn:
                if message['role'] == 'user' or (message['role'] == 'assistant' and (probing_question_type == 'information_extraction' or
                                                                                     probing_question_type == 'multi_session_reasoning' or
                                                                                     probing_question_type == 'summarization')):
                    chat_history += f"chat_id: {message['id']}, {message['role'].upper()}: {message['content']} \n\n"

            chat_history += "\n\n"

            token_num = len(_get_token_encoder().encode(chat_history))
            max_tokens = 27000 // len(selected_turns)

            if token_num > max_tokens:
                if token_num < (200000 // len(selected_turns)):
                    prompt = f"""Summarize the following conversation in NO MORE than {max_tokens} tokens. 
                            Focus on key decisions, important information, and progress made. Be concise but preserve important context.
                            CRITICAL NOTE: When providing summary, include "chat_id: chat_id_number" for each turn you include in the summary.
                            CRITICAL NOTE: DO NOT COMBINE chat_ids together as far as you can like: chat_id: x-x+5
                            Conversation: {chat_history}
                            NOTE: keep under {max_tokens} tokens.
                            NOTE: Just provide the summary without any explanation before and after the summary."""

                    chat_history = llm.invoke(prompt).content.strip()
                else:
                    chat_history = chat_history[:5000]

            chats.append(chat_history)

    bullet_texts = "\n\n".join(bullets)
    chat_texts = "\n\n\n\n".join(chats)
    prompts = []

    if probing_question_type == "multi_session_reasoning":
        prompt = multi_session_reasoning_probing_question_easy_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)
        prompt = multi_session_reasoning_probing_question_medium_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)
        prompt = multi_session_reasoning_probing_question_hard_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)

    elif probing_question_type == "temporal_reasoning":
        prompt = temporal_reasoning_probing_question_easy_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)
        prompt = temporal_reasoning_probing_question_medium_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)
        prompt = temporal_reasoning_probing_question_hard_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)

    elif probing_question_type == "event_ordering":
        prompt = event_ordering_probing_question_easy_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)
        prompt = event_ordering_probing_question_medium_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)
        prompt = event_ordering_probing_question_hard_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)

    elif probing_question_type == "summarization":
        prompt = summarization_probing_question_easy_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)
        prompt = summarization_probing_question_medium_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)
        prompt = summarization_probing_question_hard_prompt\
            .replace("<bullet_points>", bullet_texts)\
            .replace("<conversation_turns>", chat_texts)
        prompts.append(prompt)

    datas = []

    for prompt in prompts:
        response = llm.invoke(prompt).content

        data = json.loads(repair_json(response))
        datas.append(data)

    return datas


def ten_m_run_probing_question_parallel(chats_directory: str,
                                        model: str):

    question_types = ["information_extraction", "multi_session_reasoning", "knowledge_update",
                      "temporal_reasoning", "preference_following", "event_ordering",
                      "contradiction_resolution", "summarization", "instruction_following"]

    with ThreadPoolExecutor(max_workers=len(question_types)+1) as executor:
        futures = {
            executor.submit(
                ten_m_generate_probing_questions_candidate,
                chats_directory=chats_directory,
                probing_question_type=q,
                llm_name=model,
            ): q
            for q in question_types
        }

        for future in as_completed(futures):
            qtype = futures[future]
            try:
                result = future.result()
            except Exception as e:
                print(f"[{qtype}] generated an exception: {e!r}")

    plan_cutoff_address = os.path.join(chats_directory, "plan_cutoff.txt")
    with open(plan_cutoff_address, "r") as f:
        plan_cutoff = f.read().strip()
    plan_cutoff = int(plan_cutoff)
        
    dirs = sorted([
        name for name in os.listdir(chats_directory)
        if (os.path.isdir(os.path.join(chats_directory, name)) and ('plan' in name))
    ])

    dirs = dirs[:plan_cutoff]

    for dir_index, dir in enumerate(dirs):
        print(f"Abstention: {dir_index}")
        if os.path.exists(os.path.join(chats_directory, dir, "chat_trunecated.json")):
            chat_address = os.path.join(chats_directory, dir, "chat_trunecated.json")
        else:
            chat_address = os.path.join(chats_directory, dir, "chat.json")
            
        if os.path.exists(os.path.join(chats_directory, dir, "plan_new_trunecated.pickle")):
            plan_address = os.path.join(
                chats_directory, dir, "plan_new_trunecated.pickle")
        else:
            plan_address = os.path.join(
                chats_directory, dir, "plan_new.pickle")

        response = generate_probing_questions(chat_address=chat_address,
                                              indexes=[],
                                              bullets=[],
                                              probing_question_type="abstention",
                                              llm_name=model,
                                              plan_address=plan_address)

        abstention_save_address = os.path.join(
            chats_directory, f"probing_questions/plan_{dir_index}/abstention/abstention.json")
        os.makedirs(os.path.dirname(abstention_save_address), exist_ok=True)
        with open(abstention_save_address, 'w') as f:
            json.dump([response], f, indent=4)


def ten_m_create_probing_questions(chats_directory: str,
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
            futures.append(
                executor.submit(
                    ten_m_run_probing_question_parallel,
                    chats_directory=os.path.join(chats_directory, dir),
                    model=model,
                )
            )

        for future in as_completed(futures):
            try:
                result = future.result()
            except Exception as e:
                print("Task raised exception:", e)


def ten_m_add_special_bullets_to_plan(chat_directory: str):

    dirs = sorted([
        name for name in os.listdir(chat_directory)
        if os.path.isdir(os.path.join(chat_directory, name))
    ])

    def process_directory(dir_name):
        plan_address = os.path.join(chat_directory, dir_name, "plan")
        add_special_bullets_to_plan(plan_address=plan_address, llm_name="gpt")

    with ThreadPoolExecutor() as executor:
        executor.map(process_directory, dirs)
