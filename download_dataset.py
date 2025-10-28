import os
os.environ["HF_HUB_DISABLE_XET"] = "1"
import pickle
import json
import ast
from datasets import load_dataset, load_from_disk


def download_dataset():
    dataset = load_dataset("Mohammadta/BEAM")

    dataset.save_to_disk("./beam_dataset")


def download_10M_dataset():
    dataset = load_dataset("Mohammadta/BEAM-10M")

    dataset.save_to_disk("./beam_10M_dataset")


def create_conversations():
    download_dataset()

    dataset = load_from_disk("./beam_dataset")

    num_conversations = 0
    os.makedirs("test_chats", exist_ok=True)
    sizes = ["100K", "500K", "1M"]
    for size in sizes:
        conversations = dataset[size]
        for conversation in conversations:
            conversation_id = conversation['conversation_id']
            topic = conversation['conversation_seed']
            labels = conversation['narratives']
            main_sepc = conversation['user_profile']['user_info']
            relationships = conversation['user_profile']['user_relationships']
            plan_new = conversation['conversation_plan']
            user_messages = conversation['user_questions']
            chat = conversation['chat']
            probing_questions = conversation['probing_questions']

            conversation_dir = os.path.join(
                "test_chats", size, conversation_id)
            os.makedirs(conversation_dir, exist_ok=True)

            chat_dir = os.path.join(conversation_dir, "chat.json")
            with open(chat_dir, "w", encoding="utf-8") as f:
                json.dump(chat, f, ensure_ascii=False, indent=4)

            chat_dir = os.path.join(conversation_dir, "chat.pickle")
            with open(chat_dir, "wb") as f:
                pickle.dump(chat, f)

            labels_dir = os.path.join(conversation_dir, "labels.txt")
            with open(labels_dir, "w", encoding="utf-8") as f:
                f.write(labels)

            main_spec_dir = os.path.join(conversation_dir, "main_spec.txt")
            with open(main_spec_dir, "w", encoding="utf-8") as f:
                f.write(main_sepc)

            plan_dir = os.path.join(conversation_dir, "plan_new.txt")
            with open(plan_dir, "w", encoding="utf-8") as f:
                f.write(plan_new)
            plan_dir = os.path.join(conversation_dir, "plan_new.pickle")
            with open(plan_dir, "wb") as f:
                pickle.dump(plan_new, f)

            relationships_dir = os.path.join(
                conversation_dir, "relationships.txt")
            with open(relationships_dir, "w", encoding="utf-8") as f:
                f.write(relationships)

            topic_dir = os.path.join(conversation_dir, "topic.json")
            with open(topic_dir, "w", encoding="utf-8") as f:
                json.dump(topic, f, ensure_ascii=False, indent=4)

            user_messages_dir = os.path.join(
                conversation_dir, "user_messages.json")
            with open(user_messages_dir, "w", encoding="utf-8") as f:
                json.dump(user_messages, f, ensure_ascii=False, indent=4)
            user_messages_dir = os.path.join(
                conversation_dir, "user_messages.pickle")
            with open(user_messages_dir, "wb") as f:
                pickle.dump(user_messages, f)

            probing_questions_dir = os.path.join(
                conversation_dir, "probing_questions")
            os.makedirs(probing_questions_dir, exist_ok=True)
            probing_questions_dir = os.path.join(
                probing_questions_dir, "probing_questions.json")
            probing_questions_data = ast.literal_eval(probing_questions)
            with open(probing_questions_dir, "w", encoding="utf-8") as f:
                json.dump(probing_questions_data, f,
                          ensure_ascii=False, indent=4)

            num_conversations += 1

            print(f"chat {conversation_dir} is created!")

    print(f"{num_conversations} conversations were created!")


def create_10M_conversations():
    download_10M_dataset()

    dataset = load_from_disk("./beam_10M_dataset")

    num_conversations = 0

    conversations = dataset["10M"]
    for conversation in conversations:
        conversation_id = conversation['conversation_id']
        topic = conversation['conversation_seed']
        main_sepc = conversation['user_profile']['user_info']
        relationships = conversation['user_profile']['user_relationships']
        chat = conversation['chat']
        probing_questions = conversation['probing_questions']
        plans = conversation['plans']

        conversation_dir = os.path.join(
            "test_chats", "10M", conversation_id)
        os.makedirs(conversation_dir, exist_ok=True)

        chat_dir = os.path.join(conversation_dir, "chat.json")
        with open(chat_dir, "w", encoding="utf-8") as f:
            json.dump(chat, f, ensure_ascii=False, indent=4)
        chat_dir = os.path.join(conversation_dir, "chat.pickle")
        with open(chat_dir, "wb") as f:
            pickle.dump(chat, f)

        relationships_dir = os.path.join(
            conversation_dir, "core_relationships.txt")
        with open(relationships_dir, "w", encoding="utf-8") as f:
            f.write(relationships)
        relationships_dir = os.path.join(
            conversation_dir, "core_relationships.pickle")
        with open(relationships_dir, "wb") as f:
            pickle.dump(relationships, f)

        main_spec_dir = os.path.join(conversation_dir, "main_spec.txt")
        with open(main_spec_dir, "w", encoding="utf-8") as f:
            f.write(main_sepc)
        main_spec_dir = os.path.join(conversation_dir, "main_spec.pickle")
        with open(main_spec_dir, "wb") as f:
            pickle.dump(main_sepc, f)

        topic_dir = os.path.join(conversation_dir, "topic.json")
        with open(topic_dir, "w", encoding="utf-8") as f:
            json.dump(topic, f, ensure_ascii=False, indent=4)

        probing_questions_dir = os.path.join(
            conversation_dir, "probing_questions")
        os.makedirs(probing_questions_dir, exist_ok=True)
        probing_questions_dir = os.path.join(
            probing_questions_dir, "probing_questions.json")
        probing_questions_data = ast.literal_eval(probing_questions)
        with open(probing_questions_dir, "w", encoding="utf-8") as f:
            json.dump(probing_questions_data, f,
                      ensure_ascii=False, indent=4)

        for plan_id, plan in enumerate(plans):
            plan_dir = os.path.join(conversation_dir, f"plan-{plan_id}")
            os.makedirs(plan_dir, exist_ok=True)

            chat = plan["chat"]
            plan_new = plan["conversation_plan"]
            topic = plan["conversation_seed"]
            labels = plan["narratives"]
            new_relationships = plan["user_profile"]["user_relationships"]
            user_messages = plan["user_questions"]

            chat_dir = os.path.join(plan_dir, "chat.json")
            with open(chat_dir, "w", encoding="utf-8") as f:
                json.dump(chat, f, ensure_ascii=False, indent=4)
            chat_dir = os.path.join(plan_dir, "chat.pickle")
            with open(chat_dir, "wb") as f:
                pickle.dump(chat, f)

            labels_dir = os.path.join(plan_dir, "labels.txt")
            with open(labels_dir, "w", encoding="utf-8") as f:
                f.write(labels)

            relationships_dir = os.path.join(
                plan_dir, "new_relationships.txt")
            with open(relationships_dir, "w", encoding="utf-8") as f:
                f.write(new_relationships)
            relationships_dir = os.path.join(
                plan_dir, "new_relationships.json")
            with open(relationships_dir, "w", encoding="utf-8") as f:
                json.dump(new_relationships, f, ensure_ascii=False, indent=4)

            new_plan_dir = os.path.join(plan_dir, "plan_new.txt")
            with open(new_plan_dir, "w", encoding="utf-8") as f:
                f.write(plan_new)
            new_plan_dir = os.path.join(plan_dir, "plan_new.pickle")
            with open(new_plan_dir, "wb") as f:
                pickle.dump(plan_new, f)

            topic_dir = os.path.join(plan_dir, "topic.json")
            with open(topic_dir, "w", encoding="utf-8") as f:
                json.dump(topic, f, ensure_ascii=False, indent=4)

            user_messages_dir = os.path.join(
                plan_dir, "user_messages.json")
            with open(user_messages_dir, "w", encoding="utf-8") as f:
                json.dump(user_messages, f, ensure_ascii=False, indent=4)
            user_messages_dir = os.path.join(
                plan_dir, "user_messages.pickle")
            with open(user_messages_dir, "wb") as f:
                pickle.dump(user_messages, f)

        num_conversations += 1

        print(f"chat {conversation_dir} is created!")

    print(f"{num_conversations} conversations were created!")


create_conversations()
create_10M_conversations()
