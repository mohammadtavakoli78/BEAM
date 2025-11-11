from transformers import AutoTokenizer
import tiktoken
import json
import pickle
from concurrent.futures import ProcessPoolExecutor, as_completed
import re
import os


def chats_tokens_counter(chat_directory: str,
                         model_name: str):

    if os.path.exists(os.path.join(chat_directory, "chat_trunecated.json")):
        chat_address = os.path.join(chat_directory, "chat_trunecated.json")
    else:
        chat_address = os.path.join(chat_directory, "chat.json")

    with open(chat_address, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_token_counts = 0
    for batch_number, batch in enumerate(data):
        turns = batch['turns']
        for turn_number, turn in enumerate(turns):
            print(
                f"Batch Number: {batch_number}, Turn Number: {turn_number}")

            token_counts = count_message_tokens(messages=turn,
                                                model_name=model_name)

            total_token_counts += token_counts

    print(total_token_counts)


def count_message_tokens(messages: list,
                         model_name: str):

    if model_name.startswith("llama"):
        tok = AutoTokenizer.from_pretrained(
            "meta-llama/Llama-3.1-8B-Instruct")
        tokens = tok.apply_chat_template(
            messages, tokenize=True, add_generation_prompt=False)

        return len(tokens)

    elif model_name.startswith("qwen"):
        tok = AutoTokenizer.from_pretrained(
            "Qwen/Qwen2.5-7B-Instruct")
        tokens = tok.apply_chat_template(
            messages, tokenize=True, add_generation_prompt=False)

        return len(tokens)

    elif model_name.startswith("gemini"):
        enc = tiktoken.encoding_for_model("gpt-4o-mini")

        serialized = "".join(
            f"{m['role']}: {m['content']}\n" for m in messages)

        return len(enc.encode(serialized))

    else:
        raise ValueError(f"Unsupported model {model_name}")


def count_chats_tokens(chat_directory: str,
                       model_name: str,
                       token_limit: int):

    chat_address = os.path.join(chat_directory, "chat.json")
    plan_adress = os.path.join(chat_directory, "plan_new.pickle")

    with open(chat_address, "r", encoding="utf-8") as f:
        data = json.load(f)

    new_messages = []
    total_token_counts = 0
    has_exceeded = False
    for batch_number, batch in enumerate(data):
        turns = batch['turns']
        new_turns = []
        for turn_number, turn in enumerate(turns):
            print(
                f"Batch Number: {batch_number}, Turn Number: {turn_number}")

            token_counts = count_message_tokens(messages=turn,
                                                model_name=model_name)

            total_token_counts += token_counts

            if total_token_counts > token_limit:
                has_exceeded = True
                break
            else:
                new_turns.append(turn)

        if not has_exceeded:
            new_messages.append(batch)
        else:
            if new_turns:
                new_messages.append({
                    "batch_number": batch_number+1,
                    "turns": new_turns,
                    "time_anchor": batch['time_anchor']
                })
            break

    if has_exceeded:
        new_message_num_batches = len(new_messages)
        new_message_last_batch_length = len(new_messages[-1]['turns'])

        batch_old_messages = data[:new_message_num_batches][-1]

        with open(plan_adress, 'rb') as f:
            plans = pickle.load(f)

        output_address = os.path.join(
            chat_directory, "plan_new_trunecated.pickle")

        if new_message_last_batch_length == len(batch_old_messages['turns']):

            new_plans = plans[:new_message_num_batches]

        else:
            old_messages_turns = batch_old_messages['turns'][new_message_last_batch_length:]

            bullets_indexes = []
            for turn in old_messages_turns:
                if "," in turn[0]['index'] and turn[0]['index'].split(",")[1].isdigit():
                    bullet_number = int(turn[0]['index'].split(",")[1])
                    bullets_indexes.append(bullet_number)

            min_bullet_number = min(bullets_indexes)

            new_plans = plans[:new_message_num_batches]
            last_plan = new_plans[-1]
            last_plan_bullets = last_plan.split("\n")
            # Because of BATCH header is not min_bullet_number-1
            last_plan_bullets_new = last_plan_bullets[:min_bullet_number]

            new_plans[-1] = "\n".join(last_plan_bullets_new)

        with open(output_address, 'wb') as f:
            pickle.dump(new_plans, f)

        new_plan_text = "\n\n".join(new_plans)
        output_address = os.path.join(
            chat_directory, "plan_new_trunecated.txt")
        with open(output_address, 'w', encoding='utf-8') as f:
            f.writelines(new_plan_text)

        new_messages_pickle = []
        for batch_number, batch in enumerate(new_messages):
            turns = batch['turns']
            new_turns = []
            for turn_number, turn in enumerate(turns):
                for message in turn:
                    new_turns.append(message)

            new_messages_pickle.append(new_turns)

        output_address = os.path.join(chat_directory, "chat_trunecated.pickle")
        with open(output_address, 'wb') as f:
            pickle.dump(new_messages_pickle, f)

        output_address = os.path.join(chat_directory, "chat_trunecated.json")
        with open(output_address, 'w') as f:
            json.dump(new_messages, f, indent=4)

    print(total_token_counts)


def ten_m_count_chats_tokens(chat_directory: str,
                             model_name: str,
                             token_limit: int):

    chat_address = os.path.join(chat_directory, "chat.json")

    with open(chat_address, "r", encoding="utf-8") as f:
        data = json.load(f)

    new_messages = []
    total_token_counts = 0
    has_exceeded = False
    for plan_number, plan in enumerate(data):
        new_plan = []
        for batch_number, batch in enumerate(list(plan.values())[0]):
            turns = batch['turns']
            new_turns = []
            for turn_number, turn in enumerate(turns):
                print(
                    f"Plan Number: {plan_number}, Batch Number: {batch_number}, Turn Number: {turn_number}")

                token_counts = count_message_tokens(messages=turn,
                                                    model_name=model_name)

                total_token_counts += token_counts

                if total_token_counts > token_limit:
                    has_exceeded = True
                    break
                else:
                    new_turns.append(turn)

            if not has_exceeded:
                new_plan.append(batch)
            else:
                if new_turns:
                    new_plan.append({
                        "batch_number": batch_number+1,
                        "turns": new_turns,
                        "time_anchor": batch['time_anchor']
                    })
                break

        if not has_exceeded:
            new_messages.append(
                plan
            )
        else:
            new_messages.append({
                f"plan-{plan_number+1}": new_plan
            })
            break

    if has_exceeded:
        new_message_num_plans = len(new_messages)
        new_message_last_plan_num_batches = len(
            next(iter(new_messages[-1].values())))
        new_message_last_plan_last_batch_num_turns = len(
            next(iter(new_messages[-1].values()))[-1]['turns'])

        old_messages_num_turns = next(iter(
            data[:new_message_num_plans][-1].values()))[new_message_last_plan_num_batches-1]

        entries = os.listdir(chat_directory)
        dirs = sorted(
            [name for name in entries if os.path.isdir(
                os.path.join(chat_directory, name))],
            key=lambda x: int(re.search(r"\d+", x).group())
        )
        plan_adress = os.path.join(
            chat_directory, dirs[new_message_num_plans-1], "plan_new.pickle")

        with open(plan_adress, 'rb') as f:
            plans = pickle.load(f)

        output_address = os.path.join(
            chat_directory, dirs[new_message_num_plans-1], "plan_new_trunecated.pickle")

        if new_message_last_plan_last_batch_num_turns == len(old_messages_num_turns["turns"]):
            new_plans = plans[:new_message_last_plan_num_batches]
        else:
            old_messages_turns = old_messages_num_turns['turns'][new_message_last_plan_last_batch_num_turns:]

            bullets_indexes = []
            for turn in old_messages_turns:
                if "," in turn[0]['index'] and turn[0]['index'].split(",")[1].isdigit():
                    bullet_number = int(turn[0]['index'].split(",")[1])
                    bullets_indexes.append(bullet_number)

            min_bullet_number = min(bullets_indexes)

            new_plans = plans[:new_message_last_plan_num_batches]
            last_plan = new_plans[-1]
            last_plan_bullets = last_plan.split("\n")
            last_plan_bullets_new = last_plan_bullets[:min_bullet_number]

            new_plans[-1] = "\n".join(last_plan_bullets_new)

        with open(output_address, 'wb') as f:
            pickle.dump(new_plans, f)

        new_plan_text = "\n\n".join(new_plans)
        output_address = os.path.join(
            chat_directory, dirs[new_message_num_plans-1], "plan_new_trunecated.txt")
        with open(output_address, 'w', encoding='utf-8') as f:
            f.writelines(new_plan_text)

        new_messages_pickle = []
        for plan_number, plan in enumerate(new_messages):
            new_plan = []
            for batch_number, batch in enumerate(list(plan.values())[0]):
                turns = batch['turns']
                new_turns = []
                for turn_number, turn in enumerate(turns):
                    for message in turn:
                        new_turns.append(message)

                new_plan.append(batch)

            new_messages_pickle.append(
                plan
            )

        output_address = os.path.join(chat_directory, "chat_trunecated.pickle")
        with open(output_address, 'wb') as f:
            pickle.dump(new_messages_pickle, f)

        output_address = os.path.join(chat_directory, "chat_trunecated.json")
        with open(output_address, 'w') as f:
            json.dump(new_messages, f, indent=4)

    print(total_token_counts)


def terunicate_chats(input_directory: str,
                     model_name: str,
                     chat_size: str):

    entries = os.listdir(input_directory)
    dirs = sorted(
        [name for name in entries if os.path.isdir(
            os.path.join(input_directory, name))],
        key=lambda x: int(x))

    if chat_size == "100K":
        token_limit = 126000
    elif chat_size == "500K":
        token_limit = 499000
    elif chat_size == "1M":
        token_limit = 1040000
    elif chat_size == "10M":
        token_limit = 9990000

    if chat_size == "10M":
        function = ten_m_count_chats_tokens
    else:
        function = count_chats_tokens

    with ProcessPoolExecutor(max_workers=len(dirs)) as executor:
        futures = {
            executor.submit(
                function,
                chat_directory=os.path.join(input_directory, dir),
                model_name=model_name,
                token_limit=token_limit
            ): dir for dir in dirs
        }

        for future in as_completed(futures):
            dir = futures[future]
            try:
                result = future.result()
                print(f"{dir} finished with result: {result}")
            except Exception as e:
                print(f"{dir} raised an exception: {e}")

    for dir in dirs:
        chat_directory_address = os.path.join(input_directory, dir)

        count_chats_tokens(chat_directory=chat_directory_address,
                           model_name=model_name,
                           token_limit=token_limit)
