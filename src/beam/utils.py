import pickle
import json
import os
import shutil
from collections import OrderedDict
import re
from datetime import datetime
import tiktoken


def get_token_number(text):
    """Initialize the best available token encoder"""
    try:
        encoders_to_try = ["cl100k_base", "p50k_base", "r50k_base"]

        for encoding_name in encoders_to_try:
            try:
                encoder = tiktoken.get_encoding(encoding_name)
                print(f"Using tiktoken with {encoding_name} encoding")
                return len(encoder.encode(text))
            except:
                continue
    except:
        len(text) // 3
        pass


def extract_time_anchor(plan_text: str):

    lines = plan_text.strip().split('\n')
    first_bullet = lines[0] if lines else ""

    patterns = [
        r'Time Anchor:\*\*\s*([A-Za-z]+\s+\d{1,2},\s*\d{4})',
        r'(\d{4}-\d{1,2}-\d{1,2})',
        r'([A-Za-z]+\s+\d{1,2},\s*\d{4})',
        r'(\d{1,2}/\d{1,2}/\d{4})',
        r'(\d{1,2}-\d{1,2}-\d{4})',
    ]

    for pattern in patterns:
        match = re.search(pattern, first_bullet)
        if match:
            date_str = match.group(1)
            return parse_and_format_date(date_str)

    return None


def parse_and_format_date(date_str: str):
    """Parse various date formats and return Month-Day-Year"""

    formats_to_try = [
        '%B %d, %Y',
        '%b %d, %Y',
        '%Y-%m-%d',
        '%m/%d/%Y',
        '%m-%d-%Y',
    ]

    for fmt in formats_to_try:
        try:
            date_obj = datetime.strptime(date_str.strip(), fmt)
            return date_obj.strftime('%B-%d-%Y')
        except ValueError:
            continue

    return date_str


def convert_user_messages_pickle_to_txt(input_address: str,
                                        output_address: str) -> None:

    with open(input_address, 'rb') as f:
        batches = pickle.load(f)

    text = ""
    for index, batch in enumerate(batches):
        time_anchor = batch['time_anchor']
        messages = batch['messages']
        text += f"================================ BATCH {index+1} ================================" + "\n\n"

        for index2, message in enumerate(messages):
            if "->->" not in message:
                print(message)
            text += f"{index2+1}) " + message + "\n"

        with open(output_address, "w", encoding="utf-8") as f:
            f.writelines(text)


def convert_user_messages_pickle_to_json(input_address: str,
                                         output_address: str) -> None:

    with open(input_address, 'rb') as f:
        batches = pickle.load(f)

    all_batches = []

    for batch_index, batch in enumerate(batches, start=1):
        time_anchor = batch['time_anchor']
        messages = batch['messages'][0]
        batch_messages = []
        for message in messages:
            if "->->" not in message:
                print(f"Skipped: {message}")
                continue
            batch_messages.append({
                "role": "user",
                "content": message.strip()
            })

        all_batches.append({
            "batch": batch_index,
            "time_anchor": time_anchor,
            "messages": batch_messages
        })

    with open(output_address, "w", encoding="utf-8") as f:
        json.dump(all_batches, f, indent=4, ensure_ascii=False)


def ten_m_convert_user_messages_pickle_to_txt(input_directory: str,
                                              llm_name: str) -> None:

    entries = os.listdir(input_directory)
    dirs = [name for name in entries if os.path.isdir(
        os.path.join(input_directory, name))]

    for dir in dirs:
        user_questions_directory_address = os.path.join(
            input_directory, dir, f"user_questions_{llm_name}")
        user_questions_address = user_questions_directory_address + ".pickle"
        output_address = user_questions_directory_address + ".txt"

        convert_user_messages_pickle_to_txt(
            input_address=user_questions_address, output_address=output_address)


def unified_convert_user_messages_pickle_to_json(input_directory: str):
    entries = os.listdir(input_directory)
    dirs = [name for name in entries if os.path.isdir(
        os.path.join(input_directory, name))]

    if "10M" in input_directory:
        for dir in dirs:
            chat_directory = os.path.join(input_directory, dir)
            plan_entries = os.listdir(chat_directory)
            plan_dirs = [name for name in plan_entries if os.path.isdir(
                os.path.join(chat_directory, name))]

            for plan_dir in plan_dirs:
                user_questions_directory_address = os.path.join(
                    chat_directory, plan_dir, "user_messages")
                user_questions_address = user_questions_directory_address + ".pickle"
                output_address = user_questions_directory_address + ".json"

                convert_user_messages_pickle_to_json(
                    input_address=user_questions_address, output_address=output_address)

    else:
        for dir in dirs:
            user_questions_directory_address = os.path.join(
                input_directory, dir, "user_messages")
            user_questions_address = user_questions_directory_address + ".pickle"
            output_address = user_questions_directory_address + ".json"

            convert_user_messages_pickle_to_json(
                input_address=user_questions_address, output_address=output_address)


def convert_chats_pickle_to_txt(input_address: str,
                                output_address: str) -> None:

    with open(input_address, 'rb') as f:
        batches = pickle.load(f)

    text = ""
    for index, batch in enumerate(batches):
        text += f"================================ BATCH {index+1} ================================" + "\n\n"
        print(
            f"================================ BATCH {index+1} ================================")
        for index2, message in enumerate(batch):
            if message['role'] == 'user':
                text += f"User) " + message['content'] + "\n"
                print(f"User) " + message['content'] + "\n")
            elif message['role'] == 'assistant':
                text += f"Assistant) " + message['content'] + "\n"
                print(f"Assistant) " + message['content'] + "\n")

        with open(output_address, "w", encoding="utf-8") as f:
            f.writelines(text)


def convert_chats_pickle_to_json(input_address: str,
                                 output_address: str) -> None:

    if os.path.exists(input_address):
        with open(input_address, 'rb') as f:
            batches = pickle.load(f)

        all_dialogues = []
        for index, batch in enumerate(batches):
            batch_number = index + 1
            turns = []
            per_batch_turns = {}
            per_batch_turns['batch_number'] = batch_number
            time_anchor = None
            single_turn = []
            for index2, message in enumerate(batch):
                if "question_type" in message.keys() and message['question_type'] == "main_question" and single_turn != []:

                    if "time_anchor" in message.keys():
                        time_anchor = message['time_anchor']

                    turns.append(single_turn)
                    single_turn = []
                    single_turn.append(message)
                else:
                    single_turn.append(message)

            turns.append(single_turn)
            per_batch_turns['turns'] = turns
            per_batch_turns['time_anchor'] = time_anchor
            all_dialogues.append(per_batch_turns)

        with open(output_address, 'w') as f:
            json.dump(all_dialogues, f, indent=2)


def ten_m_convert_chats_pickle_to_json(input_directory: str,
                                       llm_name: str) -> None:

    entries = os.listdir(input_directory)
    dirs = [name for name in entries if os.path.isdir(
        os.path.join(input_directory, name))]

    for dir in dirs:
        chat_directory_address = os.path.join(
            input_directory, dir, f"chat_{llm_name}")
        chat_address = chat_directory_address + ".pickle"
        output_address = chat_directory_address + ".json"
        convert_chats_pickle_to_json(
            input_address=chat_address, output_address=output_address)


def unified_convert_chats_pickle_to_json(input_directory: str):
    entries = os.listdir(input_directory)
    dirs = [name for name in entries if os.path.isdir(
        os.path.join(input_directory, name))]

    if "10M" in input_directory:
        for dir in dirs:
            chat_directory = os.path.join(input_directory, dir)
            plan_entries = os.listdir(chat_directory)
            plan_dirs = [name for name in plan_entries if os.path.isdir(
                os.path.join(chat_directory, name))]

            for plan_dir in plan_dirs:
                chat_directory_address = os.path.join(
                    chat_directory, plan_dir, "chat")
                chat_address = chat_directory_address + ".pickle"
                output_address = chat_directory_address + ".json"

                convert_chats_pickle_to_json(
                    input_address=chat_address, output_address=output_address)
    else:
        for dir in dirs:
            chat_directory_address = os.path.join(
                input_directory, dir, "chat")
            chat_address = chat_directory_address + ".pickle"
            output_address = chat_directory_address + ".json"
            convert_chats_pickle_to_json(
                input_address=chat_address, output_address=output_address)


def add_ids_to_chats(input_directory: str,
                     output_address: str):

    with open(input_directory, "r", encoding="utf-8") as f:
        data = json.load(f, object_pairs_hook=OrderedDict)

    msg_id = 0
    for batch in data:
        for turn in batch.get('turns', []):
            for msg in turn:
                new_msg = OrderedDict()
                for key, val in msg.items():
                    new_msg[key] = val
                    if key == 'role':
                        new_msg['id'] = msg_id
                        msg_id += 1

                msg.clear()
                msg.update(new_msg)

    with open(output_address, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def convert_txt_plan_to_pickle(chat_directory: str):
    input_pickle_plan_address = os.path.join(chat_directory, "plan_new.pickle")
    with open(input_pickle_plan_address, 'rb') as f:
        pickle_plans = pickle.load(f)

    input_plan_address = os.path.join(chat_directory, "plan_new.txt")
    with open(input_plan_address, 'r') as f:
        plans = f.read()

    raw_batches = re.split(r'(BATCH \d+ PLAN)', plans)

    plans = []
    for i in range(1, len(raw_batches), 2):
        header = raw_batches[i].strip()
        content = raw_batches[i + 1].strip()
        plans.append(f"{header}\n{content}")

    output_plan_address = os.path.join(chat_directory, "plan_new.pickle")
    with open(output_plan_address, 'wb') as f:
        pickle.dump(plans, f)

    print(plans)


def check_plans_completness(chat_directory: str,
                            num_batches: int):

    entries = os.listdir(chat_directory)
    dirs = sorted(
        [name for name in entries if os.path.isdir(
            os.path.join(chat_directory, name))],
        key=lambda x: int(x)
    )

    for dir in dirs:
        if "10M" in chat_directory:
            plan_directory = os.path.join(chat_directory, dir)
            plan_entries = os.listdir(plan_directory)
            plan_dirs = sorted(
                [name for name in plan_entries if os.path.isdir(
                    os.path.join(plan_directory, name))]
            )
            for plan_dir in plan_dirs:
                specific_plan_directory = os.path.join(
                    plan_directory, plan_dir)
                plan_address = os.path.join(
                    specific_plan_directory, "plan_new.pickle")
                with open(plan_address, 'rb') as f:
                    pickle_plans = pickle.load(f)
                if len(pickle_plans) != num_batches:
                    print(plan_address)

        else:
            plan_directory = os.path.join(chat_directory, dir)
            plan_address = os.path.join(plan_directory, "plan_new.pickle")
            with open(plan_address, 'rb') as f:
                pickle_plans = pickle.load(f)
            if len(pickle_plans) != num_batches:
                print(plan_address)


def combine_10m_chats(input_directory: str):
    entries = os.listdir(input_directory)
    dirs = sorted(
        [name for name in entries if os.path.isdir(
            os.path.join(input_directory, name))],
        key=lambda x: int(x))

    if "10M" in input_directory:
        for dir in dirs:
            chat_directory = os.path.join(input_directory, dir)
            plan_entries = os.listdir(chat_directory)
            plan_dirs = sorted([name for name in plan_entries if os.path.isdir(
                os.path.join(chat_directory, name))])

            new_chat = []
            last_id = 0
            for plan_number, plan_dir in enumerate(plan_dirs):
                chat_directory_address = os.path.join(
                    chat_directory, plan_dir, "chat")
                chat_address = chat_directory_address + ".json"

                with open(chat_address, 'r') as file:
                    data = json.load(file)

                if last_id != 0:
                    for batch_number, batch in enumerate(data):
                        turns = batch['turns']
                        new_turns = []
                        for turn_number, turn in enumerate(turns):
                            for message_number, message in enumerate(turn):
                                data[batch_number]['turns'][turn_number][message_number]['id'] += last_id + 1

                last_id = data[-1]['turns'][-1][-1]["id"]

                new_chat.append({
                    f"plan-{plan_number+1}": data
                })

            output_address = os.path.join(chat_directory, "chat.json")
            with open(output_address, 'w') as f:
                json.dump(new_chat, f, indent=4)

            output_address = os.path.join(chat_directory, "chat.pickle")
            with open(output_address, 'wb') as f:
                pickle.dump(new_chat, f)
