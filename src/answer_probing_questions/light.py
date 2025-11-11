import os
os.environ["HF_HUB_DISABLE_XET"] = "1"
import pickle
from langchain_experimental.text_splitter import SemanticChunker
from concurrent.futures import ThreadPoolExecutor, as_completed

from src.prompts import *


def create_scratch_pad(messages: list,
                       chat_size: str,
                       qwen_llm,
                       gpt_llm):
    scratch_pads = []

    def process_pair(pair, conversation_history, id):
        print(f"Id: {id}")

        latest_user_message = pair[0]["content"]
        if len(pair) == 2:
            if (len(pair[1]["content"]) // 3.7) <= 24000:
                latest_assistant_message = pair[1]["content"]
            else:
                latest_assistant_message = pair[1]["content"][:70000]
        else:
            latest_assistant_message = "N/A"

        history = ""
        for message in conversation_history:
            history += f"{message['role'].upper()}: {message['content']} \n"

        remain_tokens = 27000 - (len(latest_assistant_message) // 3.7)

        if (len(history) // 3.7) > remain_tokens:
            remain_tokens -= 2000
            remain_tokens = int(remain_tokens * 3.7)
            history = history[-remain_tokens:]

        prompt = scratchpad_generation_prompt.replace("<history>", history) \
                                             .replace("<latest_user_message>", latest_user_message) \
                                             .replace("<latest_assistant_message>", latest_assistant_message)

        response = qwen_llm.invoke(prompt).content

        return {
            "id": id,
            "response": response
        }

    tasks = []
    if chat_size == "10M":
        for plan_number, plan in enumerate(messages):
            for batch_number, batch in enumerate(list(plan.values())[0]):
                turns = batch['turns']
                for turn_number, turn in enumerate(turns):
                    pairs = [turn[i:i+2] for i in range(0, len(turn), 2)]
                    for pair_number, pair in enumerate(pairs):
                        try:
                            if pair_number == 0:
                                if turn_number > 0:
                                    conversation_history = batch['turns'][turn_number - 1]
                                elif turn_number == 0 and batch_number > 0:
                                    conversation_history = list(plan.values())[
                                        0][batch_number - 1]['turns'][-1]
                                else:
                                    conversation_history = []
                            else:
                                conversation_history = []
                                for idx, new_pair in enumerate(pairs[:pair_number]):
                                    conversation_history.extend(new_pair)
                        except Exception as e:
                            print(e)

                        if "id" in pair[0].keys():
                            id = pair[0]['id']
                        else:
                            id = f"{batch_number}, {turn_number}, {pair_number}"
                        tasks.append(
                            (pair, conversation_history, id))
    else:
        for batch_number, batch in enumerate(messages):
            turns = batch['turns']
            for turn_number, turn in enumerate(turns):
                pairs = [turn[i:i+2] for i in range(0, len(turn), 2)]
                for pair_number, pair in enumerate(pairs):
                    if pair_number == 0:
                        if turn_number > 0:
                            conversation_history = batch['turns'][turn_number - 1]
                        elif turn_number == 0 and batch_number > 0:
                            conversation_history = messages[batch_number -
                                                            1]['turns'][-1]
                        else:
                            conversation_history = []
                    else:
                        conversation_history = []
                        for idx, new_pair in enumerate(pairs[:pair_number]):
                            conversation_history.extend(new_pair)

                    if "id" in pair[0].keys():
                        id = pair[0]['id']
                    else:
                        id = f"{batch_number}, {turn_number}, {pair_number}"
                    tasks.append(
                        (pair, conversation_history, id))

    with ThreadPoolExecutor(max_workers=25) as executor:
        futures = [executor.submit(process_pair, *t)
                   for t in tasks]
        for future in as_completed(futures):
            scratch_pads.append(future.result())

    scratch_pads = sorted(scratch_pads, key=lambda x: x["id"])

    mode = "iterative"

    tokens_limit = 14000
    if mode == "all_at_once":
        content = ""
        for scratch_pad in scratch_pads:
            content += scratch_pad["response"] + "\n\n"

        prompt = scratchpad_summarizer_all_at_once_prompt.replace("<content>", content) \
                                                         .replace("<tokens_limit>", tokens_limit)

        response = gpt_llm.invoke(prompt).content

        return response

    elif mode == "iterative":
        content = ""
        for index, scratch_pad in enumerate(scratch_pads):
            print(f"Summary Index: {index}")
            content += scratch_pad["response"] + "\n\n"

            if len(content) // 3.7 > tokens_limit*2:
                prompt = scratchpad_summarizer_iterative_prompt.replace("<content>", content) \
                                                               .replace("<tokens_limit>", tokens_limit)

                response = gpt_llm.invoke(prompt).content

                content = response

        return content


def create_episodic_memory(messages: list,
                           chat_size: str,
                           qwen_llm,
                           gpt_llm):
    tasks = []

    generation_type = "parallel"

    if generation_type == "parallel":
        def process_pair(batch_number, turn_number, pair_number, id, pair, conversation_history):

            history = ""
            for message in conversation_history:
                history += f"{message['role'].upper()}: {message['content']} \n"

            print(
                f"Batch Number: {batch_number}, Turn Number: {turn_number}")

            text = ""
            if len(pair) == 2:
                if (len(pair[1]["content"]) // 3.7) <= 24000:
                    text = f"""
                            USER: {pair[0]["content"]} \n\n
                            ASSISTAN: {pair[1]["content"]}
                            """
                else:
                    text = f"""
                            USER: {pair[0]["content"]} \n\n
                            ASSISTAN: {pair[1]["content"][:70000]}
                            """
            else:
                text = f"""
                        USER: {pair[0]["content"]} \n\n
                        ASSISTAN: N/A
                        """

            remain_tokens = 27000 - (len(text) // 3.7)

            if (len(history) // 3.7) > remain_tokens:
                remain_tokens -= 2000
                remain_tokens = int(remain_tokens * 3.7)
                history = history[-remain_tokens:]

            prompt = f""" I provide you with a text. Your task it to identify all the details stated in the text,
                        and output that in key: value format.
                        E.g.:
                        Key 1: Value 1,
                        Key 2: Value 2,
                        Key 3: Value 3,
                        ....

                        Also at the end, I want to provide a brieft summary of what this text was about in this format: Summary: 'summarized text'

                        Note: only ouput key-values and the summary. DO NOT provide any explanation before or after that.
                        Note: Do not ouput Key 1, Key 2, ...

                        **Previous Context:**
                        {history}

                        text: {text}
                        """

            response = qwen_llm.invoke(prompt).content

            return {
                "text": response,
                "original_text": {
                    "text": text,
                    "id": id
                },
                "metadata": {
                    "id": id,
                    "batch_number": batch_number+1,
                    "turn_number": turn_number+1,
                    "pair_number": pair_number+1
                }
            }

        if chat_size == "10M":
            for plan_number, plan in enumerate(messages):
                for batch_number, batch in enumerate(list(plan.values())[0]):
                    turns = batch['turns']
                    for turn_number, turn in enumerate(turns):
                        pairs = [turn[i:i+2] for i in range(0, len(turn), 2)]
                        for pair_number, pair in enumerate(pairs):
                            if pair_number == 0:
                                if turn_number > 0:
                                    conversation_history = batch['turns'][turn_number - 1]
                                elif turn_number == 0 and batch_number > 0:
                                    conversation_history = list(plan.values())[
                                        0][batch_number - 1]['turns'][-1]
                                else:
                                    conversation_history = []
                            else:
                                conversation_history = []
                                for idx, new_pair in enumerate(pairs[:pair_number]):
                                    conversation_history.extend(new_pair)

                            id = f"{batch_number}, {turn_number}, {pair_number}"
                            tasks.append(
                                (batch_number, turn_number, pair_number, id, pair, conversation_history))
        else:
            for batch_number, batch in enumerate(messages):
                turns = batch['turns']
                for turn_number, turn in enumerate(turns):
                    pairs = [turn[i:i+2] for i in range(0, len(turn), 2)]
                    for pair_number, pair in enumerate(pairs):
                        if pair_number == 0:
                            if turn_number > 0:
                                conversation_history = batch['turns'][turn_number - 1]
                            elif turn_number == 0 and batch_number > 0:
                                conversation_history = messages[batch_number -
                                                                1]['turns'][-1]
                            else:
                                conversation_history = []
                        else:
                            conversation_history = []
                            for idx, new_pair in enumerate(pairs[:pair_number]):
                                conversation_history.extend(new_pair)

                        id = f"{batch_number}, {turn_number}, {pair_number}"
                        tasks.append(
                            (batch_number, turn_number, pair_number, id, pair, conversation_history))

        chunks = []
        with ThreadPoolExecutor(max_workers=25) as executor:
            futures = [executor.submit(process_pair, *t)
                       for t in tasks]
            for future in as_completed(futures):
                chunks.append(future.result())

        return chunks

    else:
        if chat_size == "10M":
            for plan_number, plan in enumerate(messages):
                for batch_number, batch in enumerate(list(plan.values())[0]):
                    turns = batch['turns']
                    for turn_number, turn in enumerate(turns):
                        print(
                            f"Batch Number: {batch_number}, Turn Number: {turn_number}")
                        for message in turn:
                            pairs = [turn[i:i+2]
                                     for i in range(0, len(turn), 2)]

                            for pair_number, pair in enumerate(pairs):
                                if len(pair) == 2:
                                    if (len(pair[1]["content"]) // 3.7) <= 24000:
                                        text = f"""
                                        USER: {pair[0]["content"]} \n\n
                                        ASSISTANT: {pair[1]["content"]}
                                        """
                                    else:
                                        text = f"""
                                        USER: {pair[0]["content"]} \n\n
                                        ASSISTANT: {pair[1]["content"][:70000]}
                                        """
                                else:
                                    text = f"""
                                    USER: {pair[0]["content"]} \n\n
                                    ASSISTANT: N/A
                                    """

                                prompt = kv_creation_prompt.replace(
                                    "<input_text>", text)

                                response = qwen_llm.invoke(prompt).content

                                chunks.append({
                                    "text": response,
                                    "metadata": {"batch_number": batch_number, "turn_number": turn_number}
                                })
        else:
            for batch_number, batch in enumerate(messages):
                turns = batch['turns']
                for turn_number, turn in enumerate(turns):
                    print(
                        f"Batch Number: {batch_number}, Turn Number: {turn_number}")
                    for message in turn:
                        pairs = [turn[i:i+2]
                                 for i in range(0, len(turn), 2)]
                        for pair_number, pair in enumerate(pairs):
                            if (len(pair[1]["content"]) // 3.7) <= 24000:
                                text = f"""
                                USER: {pair[0]["content"]} \n\n
                                ASSISTANT: {pair[1]["content"]}
                                """
                            else:
                                text = f"""
                                USER: {pair[0]["content"]} \n\n
                                ASSISTANT: {pair[1]["content"][:70000]}
                                """

                            prompt = kv_creation_prompt.replace(
                                "<input_text>", text)

                            response = qwen_llm.invoke(prompt).content

                            chunks.append({
                                "text": response,
                                "metadata": {"batch_number": batch_number, "turn_number": turn_number}
                            })


def create_working_memory(messages: list,
                          chat_size: str):
    chunks = []
    short_term_chunks = None

    if chat_size == "10M":
        for plan_number, plan in enumerate(messages):
            for batch_number, batch in enumerate(list(plan.values())[0]):
                turns = batch['turns']
                for turn_number, turn in enumerate(turns):
                    for message in turn:
                        pairs = [turn[i:i+2]
                                 for i in range(0, len(turn), 2)]
                        for pair_number, pair in enumerate(pairs):
                            if len(pair) == 2:
                                text = f"""
                                USER: {pair[0]["content"]} \n\n
                                ASSISTANT: {pair[1]["content"]}
                                """
                            else:
                                text = f"""
                                USER: {pair[0]["content"]} \n\n
                                ASSISTANT: N/A
                                """
                            chunks.append({
                                "text": text,
                                "metadata": {"batch_number": batch_number+1, "turn_number": turn_number+1, "pair_number": pair_number+1, "type": "short_tern"}
                            })
    else:
        for batch_number, batch in enumerate(messages):
            turns = batch['turns']
            for turn_number, turn in enumerate(turns):
                for message in turn:
                    pairs = [turn[i:i+2]
                             for i in range(0, len(turn), 2)]
                    for pair_number, pair in enumerate(pairs):
                        text = f"""
                        USER: {pair[0]["content"]} \n\n
                        ASSISTANT: {pair[1]["content"]}
                        """
                        chunks.append({
                            "text": text,
                            "metadata": {"batch_number": batch_number+1, "turn_number": turn_number+1, "pair_number": pair_number+1, "type": "short_tern"}
                        })

    short_term_chunks = chunks[-100:]
    short_term_texts = [c["text"] for c in short_term_chunks]
    short_term_metas = [c["metadata"] for c in short_term_chunks]

    return short_term_chunks, short_term_texts, short_term_metas


def create_memory_chunks(messages: list,
                         chat_size: str,
                         scratchpad_save_address: str,
                         qwen_llm,
                         gpt_llm):

    scratch_pad = ""
    chunks = []
    short_term_chunks = None

    # ================================ Scratchpad ================================
    file_address = os.path.join(
        scratchpad_save_address, "scrach_pad_new.txt")

    if os.path.isfile(file_address):
        with open(file_address, "r") as f:
            scratch_pad = f.read()
    else:
        scratch_pad = create_scratch_pad(messages=messages,
                                         chat_size=chat_size,
                                         qwen_llm=qwen_llm,
                                         gpt_llm=gpt_llm)

        with open(file_address, "w") as f:
            f.write(scratch_pad)

    # ================================ Episodic memory ================================
    long_term_chunks_address = os.path.join(
        scratchpad_save_address, "long_term_chunks.pkl")
    if os.path.isfile(long_term_chunks_address):
        with open(long_term_chunks_address, "rb") as f:
            long_term_chunks = pickle.load(f)

            long_term_original_texts = [
                c["original_text"] for c in long_term_chunks]
            long_term_texts = [c["text"] for c in long_term_chunks]
            long_term_metas = [c["metadata"] for c in long_term_chunks]
    else:
        long_term_chunks = []
        long_term_chunks = create_episodic_memory(messages=messages,
                                                  chat_size=chat_size,
                                                  qwen_llm=qwen_llm,
                                                  gpt_llm=gpt_llm)
        long_term_original_texts = [
            c["original_text"] for c in long_term_chunks]
        long_term_texts = [c["text"] for c in long_term_chunks]
        long_term_metas = [c["metadata"] for c in long_term_chunks]

        with open(long_term_chunks_address, "wb") as f:
            pickle.dump(long_term_chunks, f)

    # ================================ Working memory ================================
    short_term_chunks, short_term_texts, short_term_metas = create_working_memory(messages=messages,
                                                                                  chat_size=chat_size)

    chunks = long_term_chunks
    texts = long_term_texts + short_term_texts
    metas = long_term_metas + short_term_metas

    return chunks, short_term_chunks, scratch_pad


def noise_filtering(result: list,
                    chunks: list,
                    short_term_chunks: list,
                    scratch_pad: str,
                    query,
                    qwen_llm,
                    embedding):

    context = ""
    reader_max_tokens = 14000
    # reader_max_tokens = 28000

    scratch_pad_num_tokens = len(scratch_pad) // 3.5
    long_term_original_texts = []
    for c in chunks:
        if "original_text" in c.keys():
            long_term_original_texts.append(c['original_text'])

    final_results = []
    for doc in result:
        if "type" in doc.metadata:
            final_results.append({
                "text": doc.page_content
            })
        else:
            id = doc.metadata["id"]
            for obj in long_term_original_texts:
                obj_id = obj["id"].strip()
                if obj_id == id.strip():

                    final_results.append({
                        "text": obj['text']
                    })

    noise_handling_type = 1

    selected_docs = []
    if noise_handling_type == 1:
        chunker = SemanticChunker(
            embeddings=embedding,
            buffer_size=1,
            breakpoint_threshold_type="percentile",
            breakpoint_threshold_amount=80.0
        )
        docs = chunker.create_documents([scratch_pad])

        for doc in docs:
            doc_text = doc.page_content

            prompt = filter_chunk_context_prompt.replace("<query>", query) \
                                                .replace("<doc_text>", doc_text)

            response = qwen_llm.invoke(prompt).content.strip().lower()

            if response == "yes":
                selected_docs.append(doc_text)

    elif noise_handling_type == 2:
        prompt = filter_all_context_prompt.replace("<query>", query) \
            .replace("<scratch_pad>", scratch_pad)

        response = qwen_llm.invoke(prompt).content.strip().lower()
        selected_docs.append(response)
    elif noise_handling_type == 3:
        pass

    # context += f"\n\n\n SCRATCH PAD: N/A"
    for document in final_results:
        if (len(context + document['text'])) // 3.5 < reader_max_tokens:
            context += document['text'] + "\n\n"

    for obj in short_term_chunks:
        if (len(context + obj['text'])) // 3.5 < reader_max_tokens:
            context += obj['text'] + "\n\n"

    scratch_pad = "\n\n".join(selected_docs)
    context += f"\n\n\n SCRATCH PAD: {scratch_pad}"

    return context
