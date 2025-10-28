import json
import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
import time
import traceback
import argparse

from evaluation import *
from llm import gpt_llm


def get_rubric(probing_questions_address: str,
               key: str,
               index: int):

    with open(probing_questions_address, "r") as f:
        data = json.load(f)

    return data[key][index]['rubric']


def run_evaluation(probing_questions_address: str,
                   answers_directory: str,
                   output_address: str,
                   model):

    with open(answers_directory, "r") as f:
        data = json.load(f)

    values = {}
    for key in data.keys():
        print(f"Question Type: {key}")

        temp_data = []
        questions = data[key]
        for index, question in enumerate(questions):
            print(f"Question Index: {index}")

            rubric = get_rubric(probing_questions_address=probing_questions_address,
                                key=key,
                                index=index)

            llm_response = question["llm_response"]
            probing_question = question["question"]

            initialize_models()

            if key == "abstention":
                result = evaluate_abstention(rubric=rubric, llm_response=llm_response, probing_question=probing_question,
                                             model=model)
            elif key == "contradiction_resolution":
                result = evaluate_contradiction_resolution(rubric=rubric, llm_response=llm_response, probing_question=probing_question,
                                                           model=model)
            elif key == "event_ordering":
                result = evaluate_event_ordering(rubric=rubric, llm_response=llm_response, probing_question=probing_question,
                                                 model=model)
            elif key == "information_extraction":
                result = evaluate_information_extraction(rubric=rubric, llm_response=llm_response, probing_question=probing_question,
                                                         model=model)
            elif key == "instruction_following":
                result = evaluate_instruction_following(rubric=rubric, llm_response=llm_response, probing_question=probing_question,
                                                        model=model)
            elif key == "knowledge_update":
                result = evaluate_knowledge_update(rubric=rubric, llm_response=llm_response, probing_question=probing_question,
                                                   model=model)
            elif key == "multi_session_reasoning":
                result = evaluate_multi_session_reasoning(rubric=rubric, llm_response=llm_response, probing_question=probing_question,
                                                          model=model)
            elif key == "preference_following":
                result = evaluate_preference_following(rubric=rubric, llm_response=llm_response, probing_question=probing_question,
                                                       model=model)
            elif key == "summarization":
                result = evaluate_summarization(rubric=rubric, llm_response=llm_response, probing_question=probing_question,
                                                model=model)
            elif key == "temporal_reasoning":
                result = evaluate_temporal_reasoning(rubric=rubric, llm_response=llm_response, probing_question=probing_question,
                                                     model=model)

            temp_data.append(result)

        values[key] = temp_data

        with open(output_address, "w", encoding="utf-8") as f:
            json.dump(values, f, indent=4)

    with open(output_address, "w", encoding="utf-8") as f:
        json.dump(values, f, indent=4)


def run_evaluation_event_ordering(probing_questions_address: str,
                                  answers_directory: str,
                                  output_address: str,
                                  model):

    with open(answers_directory, "r") as f:
        data = json.load(f)

    values = {}
    with open(output_address, "r") as f:
        values = json.load(f)

    for key in data.keys():
        if key == "event_ordering":
            print(f"Question Type: {key}")

            temp_data = []
            questions = data[key]
            for index, question in enumerate(questions):
                print(f"Question Index: {index}")

                rubric = get_rubric(probing_questions_address=probing_questions_address,
                                    key=key,
                                    index=index)

                llm_response = question["llm_response"]
                probing_question = question["question"]

                initialize_models()

                result = evaluate_event_ordering(rubric=rubric, llm_response=llm_response, probing_question=probing_question,
                                                 model=model)

                temp_data.append(result)

            values[key] = temp_data

        with open(output_address, "w", encoding="utf-8") as f:
            json.dump(values, f, indent=4)


def batch_run_evaluation(input_directory: str,
                         chat_size: str,
                         model,
                         start_index: int,
                         end_index: int,
                         max_workers: int,
                         allowed_result_files):

    entries = os.listdir(input_directory)
    dirs = sorted(
        [name for name in entries if os.path.isdir(
            os.path.join(input_directory, name))],
        key=lambda x: int(x))

    mode = 'parallel'
    tasks = []

    if mode == "parallel":
        def process_dir(input_directory, chat_size, model, dir):
            result_directory = os.path.join(input_directory, dir)
            result_files = os.listdir(result_directory)

            for result_file in result_files:
                if result_file.endswith(".json") and result_file in allowed_result_files:
                    print(f"************ Result File: {result_file}")
                    result_file_address = os.path.join(
                        result_directory, result_file)

                    output_file = "evaluation-" + result_file
                    output_address = os.path.join(
                        result_directory, output_file)

                    probing_question_address = os.path.join(
                        "chats", chat_size, dir, "probing_questions", "probing_questions.json"
                    )

                    run_evaluation(
                        probing_questions_address=probing_question_address,
                        answers_directory=result_file_address,
                        output_address=output_address,
                        model=model
                    )

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [
                executor.submit(process_dir, input_directory,
                                chat_size, model, dirs[index])
                for index in range(start_index, end_index)
            ]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(
                        "============================== ERROR ==============================")
                    print(traceback.format_exc())
                    print(f"Error while processing a directory: {e}")

    else:
        for index in range(start_index, end_index):
            dir = dirs[index]

            result_directory = os.path.join(input_directory, dir)

            result_files = os.listdir(result_directory)

            for result_file in result_files:
                if ".json" in result_file:
                    result_file_address = os.path.join(
                        result_directory, result_file)

                    output_file = "evaluation-results-" + result_file
                    output_address = os.path.join(
                        result_directory, output_file)

                    probing_questio_address = os.path.join(
                        "chats", chat_size, dir, "probing_questions", "probing_questions.json")

                    run_evaluation(probing_questions_address=probing_questio_address,
                                   answers_directory=result_file_address,
                                   output_address=output_address,
                                   model=model)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Batch evaluation of results."
    )

    parser.add_argument(
        "--input_directory",
        type=str,
        required=True,
        help="Path to the main directory containing results (e.g., results/10M)."
    )

    parser.add_argument(
        "--chat_size",
        type=str,
        required=True,
        help="Chat size (e.g., 10M, 1M, 500K, 100K)."
    )

    parser.add_argument(
        "--start_index",
        type=int,
        default=0,
        help="Start index of the directories to evaluate (default: 0)."
    )

    parser.add_argument(
        "--end_index",
        type=int,
        required=True,
        help="End index (non-inclusive) of the directories to evaluate."
    )

    parser.add_argument(
        "--max_workers",
        type=int,
        default=10,
        help="Maximum number of parallel threads (default: 10)."
    )

    parser.add_argument(
        "--allowed_result_files",
        nargs="+",
        required=True,
        help="List of result .json filenames to evaluate in each directory."
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    start = time.time()

    batch_run_evaluation(
        input_directory=args.input_directory,
        chat_size=args.chat_size,
        model=gpt_llm,
        start_index=args.start_index,
        end_index=args.end_index,
        max_workers=args.max_workers,
        allowed_result_files=args.allowed_result_files
    )

    end = time.time()

    elapsed = int(end - start)
    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60

    print(f"Elapsed time: {hours:02}:{minutes:02}:{seconds:02}")
