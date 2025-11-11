import json
import os
import pickle
import multiprocessing as mp
import argparse
import time

from src.beam.main import generate_plans, add_special_bullets_to_plan, get_labels, get_profile, user_messages_generation_fast, answer_generation
from src.beam.ten_milion_pipeline import ten_m_plan_generation, ten_m_user_messages_generation, ten_m_answer_generation
from src.llm import BuildLLm


def run_plans_generation(chats_directory: str,
                       chat_size: str,
                       index: str):

    topics_address = os.path.join(chats_directory, "topics.json")
    with open(topics_address, "r", encoding="utf-8") as f:
        data = json.load(f)

    object = data[index]

    id = str(object['id'])

    chat_address = os.path.join(chats_directory, id)
    os.makedirs(chat_address, exist_ok=True)

    chat_topic_address = os.path.join(chat_address, "topic.json")
    with open(chat_topic_address, "w", encoding="utf-8") as f:
        json.dump(object, f, indent=4)

    sub_categories = ", ".join(object["subtopics"])
    category = object["category"]
    title = object["title"]
    theme = object["theme"]
    if "timeline" in object.keys():
        timeline = object["timeline"]
    else:
        timeline = "N/A"

    if "mode" in object.keys():
        mode = object["mode"]
    else:
        mode = "similar"

    if "num_plans" in object.keys():
        NUM_PLANS = object["num_plans"]
    else:
        NUM_PLANS = 10

    topic = category + " -> " + title
    theme = theme + " -> " + sub_categories

    if category.lower() == "math":
        category = "math"
    elif category.lower() == "coding":
        category = "coding"
    else:
        category = "general"

    if chat_size != "10M":
        labels = get_labels(topic=topic, theme=theme, domain=category)

        main_spec, relationships = get_profile()

        labels_address = os.path.join(chat_address, "labels.txt")
        main_spec_address = os.path.join(chat_address, "main_spec.txt")
        relationships_address = os.path.join(
            chat_address, "relationships.txt")

        with open(labels_address, "w", encoding="utf-8") as f:
            f.write(labels)
        with open(main_spec_address, "w", encoding="utf-8") as f:
            f.write(main_spec)
        with open(relationships_address, "w", encoding="utf-8") as f:
            f.write(relationships)

    if chat_size == "100K":
        if category == "general":
            NUM_BATCHES = 5
            NUM_BULLETS = 20
        elif category == "coding":
            NUM_BATCHES = 3
            NUM_BULLETS = 23
        elif category == "math":
            NUM_BATCHES = 3
            NUM_BULLETS = 25
    elif chat_size == "500K":
        if category == "general":
            NUM_BATCHES = 10
            NUM_BULLETS = 30
        elif category == "coding":
            NUM_BATCHES = 10
            NUM_BULLETS = 30
        elif category == "math":
            NUM_BATCHES = 10
            NUM_BULLETS = 30
    elif chat_size == "1M":
        NUM_BATCHES = 10
        if category == "general":
            NUM_BULLETS = 30
        elif category == "coding":
            NUM_BULLETS = 30
        elif category == "math":
            NUM_BULLETS = 30
    elif chat_size == "10M":
        NUM_BATCHES = 10
        NUM_BULLETS = 30

    if chat_size == "10M":
        ten_m_plan_generation(initial_topic=object,
                              first_timeline=timeline,
                              num_plans=NUM_PLANS,
                              num_batches=str(NUM_BATCHES),
                              domain=category,
                              save_address=chat_address,
                              llm_name="gpt",
                              mode=mode)

        entries = os.listdir(chat_address)
        dirs = sorted(
            [name for name in entries if os.path.isdir(
                os.path.join(chat_address, name))],
            key=lambda x: int(x.split('-')[1])
        )

        for dir in dirs:
            plan_directory = os.path.join(chat_address, dir, "plan")

            add_special_bullets_to_plan(plan_address=plan_directory,
                                        num_bullets=NUM_BULLETS,
                                        llm_name="gpt")

    else:
        plan_save_address = os.path.join(chat_address, "plan")
        generate_plans(topic=topic, theme=theme, timeline=timeline, num_batches=NUM_BATCHES, num_bullets=NUM_BULLETS,
                       labels=labels, main_spec=main_spec, relationships=relationships,
                       llm_name="gpt", save_address=plan_save_address, input_address=None, domain=category)

        add_special_bullets_to_plan(plan_address=plan_save_address,
                                    num_bullets=NUM_BULLETS,
                                    llm_name="gpt")


def run_question_generation(chats_directory: str,
                            chat_size: str,
                            index: int):

    entries = os.listdir(chats_directory)

    dirs = sorted(
        [name for name in entries if os.path.isdir(
            os.path.join(chats_directory, name))],
        key=lambda x: int(x)
    )

    dir = dirs[index]

    chat_directory = os.path.join(chats_directory, dir)

    topic_address = os.path.join(chat_directory, "topic.json")
    with open(topic_address, "r", encoding="utf-8") as f:
        data = json.load(f)

    title = data['title']
    theme = data['theme']
    category = data["category"]
    sub_categories = ", ".join(data["subtopics"])
    topic = category + " -> " + title
    theme = theme + " -> " + sub_categories

    topic = topic
    theme = theme
    if category.lower() == "math":
        category = "math"
    elif category.lower() == "coding":
        category = "coding"
    else:
        category = "general"

    if chat_size == "100K":
        if category == "general":
            NUM_BATCHES = 5
            BATCH_SIZE = 20
            SUB_BATCHES_PER_BATCH = 10
        elif category == "coding":
            NUM_BATCHES = 3
            BATCH_SIZE = 23
            SUB_BATCHES_PER_BATCH = 23
        elif category == "math":
            NUM_BATCHES = 3
            BATCH_SIZE = 25
            SUB_BATCHES_PER_BATCH = 25
    elif chat_size == "500K":
        SUB_BATCHES_PER_BATCH = 10
        if category == "general":
            NUM_BATCHES = 10
            BATCH_SIZE = 40
        elif category == "coding":
            NUM_BATCHES = 10
            BATCH_SIZE = 30
        elif category == "math":
            NUM_BATCHES = 10
            BATCH_SIZE = 40
    elif chat_size == "1M":
        NUM_BATCHES = 10
        SUB_BATCHES_PER_BATCH = 10
        if category == "general":
            BATCH_SIZE = 90
        elif category == "coding":
            BATCH_SIZE = 60
        elif category == "math":
            BATCH_SIZE = 60
    elif chat_size == "10M":
        NUM_BATCHES = 10
        SUB_BATCHES_PER_BATCH = 10
        if category == "general":
            BATCH_SIZE = 90
        elif category == "coding":
            BATCH_SIZE = 60
        elif category == "math":
            BATCH_SIZE = 60

    SUB_BATCH_SIZE = BATCH_SIZE // SUB_BATCHES_PER_BATCH

    if chat_size != "10M":
        plan_address = os.path.join(chat_directory, "plan_new.pickle")
        with open(plan_address, 'rb') as f:
            plan = pickle.load(f)

        save_address = os.path.join(chat_directory, "user_messages.pickle")
        user_messages_generation_fast(topic=topic, theme=theme, plans=plan, num_batches=NUM_BATCHES,
                                      sub_batches_per_batch=SUB_BATCHES_PER_BATCH,
                                      sub_batch_size=SUB_BATCH_SIZE, batch_size=BATCH_SIZE,
                                      llm_name="llama", save_address=save_address,
                                      domain=category, sepcial_bullets=True)
    else:
        ten_m_user_messages_generation(plan_save_address=chat_directory,
                                       num_batches=NUM_BATCHES,
                                       sub_batches_per_batch=SUB_BATCHES_PER_BATCH,
                                       sub_batch_size=SUB_BATCH_SIZE,
                                       batch_size=BATCH_SIZE,
                                       llm_name="llama",
                                       domain=category,
                                       mode="parallel")


def run_answer_generation(chats_directory: str,
                          chat_size: str,
                          index: int,
                          llm):

    entries = os.listdir(chats_directory)
    dirs = sorted(
        [name for name in entries if os.path.isdir(
            os.path.join(chats_directory, name))],
        key=lambda x: int(x)
    )

    dir = dirs[index]

    chat_directory = os.path.join(chats_directory, dir)

    topic_address = os.path.join(chat_directory, "topic.json")
    with open(topic_address, "r", encoding="utf-8") as f:
        data = json.load(f)

    title = data['title']
    theme = data['theme']
    category = data["category"]
    sub_categories = ", ".join(data["subtopics"])
    topic = category + " -> " + title
    theme = theme + " -> " + sub_categories

    topic = topic
    theme = theme
    if category.lower() == "math":
        category = "math"
    elif category.lower() == "coding":
        category = "coding"
    else:
        category = "general"

    if chat_size != "10M":
        messages_address = os.path.join(
            chat_directory, "user_messages.pickle")
        output_address = os.path.join(chat_directory, "chat.pickle")
        plan_address = os.path.join(chat_directory, "plan_new.pickle")
        
        answer_generation(
            input_address=messages_address,
            output_address=output_address,
            plans_address=plan_address,
            topic=topic,
            theme=theme,
            llm=llm
        )
    else:
        ten_m_answer_generation(input_directory=chat_directory,
                                mode="parallel",
                                llm=llm)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Process answer generation parameters")

    parser.add_argument("--model_url", type=str,
                        required=True, help="URL of the VLLM server")
    parser.add_argument("--model_name", type=str,
                        required=True, help="Directory of the LLM")
    parser.add_argument("--api_key", type=str, required=True,
                        help="API key for authentication")
    parser.add_argument("--generation_stage", type=str, required=True,
                        help="Generation Stage", choices=["plan", "question", "answer"])
    parser.add_argument("--start_index", type=int,
                        required=True, help="Starting index")
    parser.add_argument("--end_index", type=int,
                        required=True, help="Ending index")
    parser.add_argument("--chats_dir", type=str, required=True,
                        help="Directory containing chats")
    parser.add_argument("--chat_size", type=str,
                        required=True, help="Size of chat")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    english_only_regex = "[\\u0000-\\u2E7F]+"

    print("Model URL:", args.model_url)
    print("Model Name:", args.model_name)
    print("API Key:", args.api_key)
    print("Generation Stage:", args.generation_stage)
    print("Start Index:", args.start_index)
    print("End Index:", args.end_index)
    print("Chats Directory:", args.chats_dir)
    print("Chat Size:", args.chat_size)

    qwen_awq_32_llm_obj = BuildLLm(model_url=args.model_url,
                                   model_name=args.model_name,
                                   api_key=args.api_key,
                                   temperature=0.1,
                                   extra_body={"guided_regex": english_only_regex})

    qwen_llm = qwen_awq_32_llm_obj.build_llm()

    start_index = args.start_index  # 0
    end_index = args.end_index  # 10
    chats_dir = args.chats_dir  # chats/10M"
    chat_size = args.chat_size  # 10M

    start = time.perf_counter()

    procs = []
    for process_num in range(start_index, end_index):
        if args.generation_stage == "plan":
            function = run_plans_generation
            p = mp.Process(
                target=function,
                args=(chats_dir, chat_size, process_num)
            )
        elif args.generation_stage == "question":
            function = run_question_generation
            p = mp.Process(
                target=function,
                args=(chats_dir, chat_size, process_num)
            )
        elif args.generation_stage == "answer":
            function = run_answer_generation
            p = mp.Process(
                target=function,
                args=(chats_dir, chat_size, process_num, qwen_llm)
            )
        p.start()
        procs.append(p)

    for p in procs:
        p.join()

    end = time.perf_counter()

    print(f"Execution time: {end - start:.4f} seconds")
