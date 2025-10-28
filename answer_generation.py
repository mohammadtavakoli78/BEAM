import json
import os
import time
import traceback
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

from llm import BuildLLm
from long_term_methods import probing_question_evaluation

model_config_default = {
    "temperature": 0,
    "api_key": "",
    "request_timeout": 60,
    "model_name": "",
    "model_provider": "",
    "max_tokens": 1000000
}

retrieval_config_default = {
    "retrieval_method": "light",
    "retriever": "dense",
    "k": 5
}


def answer_generation(probing_questions_address: str,
                      evaluation_type: str,
                      chat_address: str,
                      chat_size: str,
                      gpt_llm,
                      qwen_llm,
                      model,
                      result_save_address: str,
                      result_save_file_name: str,
                      model_config=model_config_default,
                      retrieval_config=retrieval_config_default):

    with open(probing_questions_address, 'r') as file:
        data = json.load(file)

    data_temp = {}
    output_address = os.path.join(result_save_address, result_save_file_name)

    saved_retriever = None
    saved_chunks = None
    saved_short_term_chunks = None
    saved_scratch_pad = None
    saved_messages = None
    
    for key in list(data.keys()):
        print(f"key: {key}")
        questions = data[key]
        question_type_temp = []
        for question in questions:
            try:
                if evaluation_type == "long-context":
                    response, messages = probing_question_evaluation(query=question["question"],
                                                                        chat_directory=result_save_address,
                                                                        chat_address=chat_address,
                                                                        chat_size=chat_size,
                                                                        evaluation_type=evaluation_type,
                                                                        gpt_llm=gpt_llm,
                                                                        qwen_llm=qwen_llm,
                                                                        model=model,
                                                                        model_config=model_config,
                                                                        saved_messages=saved_messages,
                                                                        retrieval_config=retrieval_config,
                                                                        saved_retriever=saved_retriever,
                                                                        chunks=saved_chunks,
                                                                        short_term_chunks=saved_short_term_chunks,
                                                                        scratch_pad=saved_scratch_pad)

                    if not saved_messages:
                        saved_messages = messages
                else:
                    response, retriever, chunks, short_term_chunks, scratch_pad = probing_question_evaluation(query=question["question"],
                                                                                            chat_directory=result_save_address,
                                                                                            chat_address=chat_address,
                                                                                            chat_size=chat_size,
                                                                                            evaluation_type=evaluation_type,
                                                                                            gpt_llm=gpt_llm,
                                                                                            qwen_llm=qwen_llm,
                                                                                            model=model,
                                                                                            model_config=model_config,
                                                                                            saved_messages=saved_messages,
                                                                                            retrieval_config=retrieval_config,
                                                                                            saved_retriever=saved_retriever,
                                                                                            chunks=saved_chunks,
                                                                                            short_term_chunks=saved_short_term_chunks,
                                                                                            scratch_pad=saved_scratch_pad)

                    if not saved_retriever:
                        saved_retriever = retriever
                        saved_chunks = chunks
                        saved_short_term_chunks = short_term_chunks
                        saved_scratch_pad = scratch_pad

            except Exception as e:
                response = f"Error in {key} question type and {question['question']} and for {output_address}"
                error_message = (
                    f"Error in {key} question type and {question['question']}\n"
                    f"Error is: {e}\n"
                    f"Traceback:\n{traceback.format_exc()}\n\n"
                )

                print(error_message)

                with open(f"{result_save_address}/error_log.txt", "a", encoding="utf-8") as f:
                    f.write(error_message)

            if evaluation_type == "long-context":
                sleep_time = model_config["sleep_time"]
                time.sleep(sleep_time)
            object_temp = question
            object_temp["llm_response"] = response
            question_type_temp.append(object_temp)

        data_temp[key] = question_type_temp
        with open(output_address, "w", encoding="utf-8") as f:
            json.dump(data_temp, f, indent=4)

    with open(output_address, "w", encoding="utf-8") as f:
        json.dump(data_temp, f, indent=4)


def batch_run_answer_generation(input_directory: str,
                                chat_size: str,
                                gpt_llm,
                                qwen_llm,
                                model,
                                evaluation_type: str,
                                result_save_file_name: str,
                                start_index: int,
                                end_index: int,
                                num_threads: int,
                                model_config,
                                retrieval_config):

    mode = "parallel"

    entries = os.listdir(input_directory)
    dirs = sorted(
        [name for name in entries
         if os.path.isdir(os.path.join(input_directory, name)) and name.isdigit()],
        key=lambda x: int(x)
    )

    if mode == "sequential":
        for index in range(start_index, end_index):
            dir = dirs[index]
            chat_directory = os.path.join(input_directory, dir)

            if os.path.exists(os.path.join(chat_directory, "chat_trunecated.json")):
                chat_address = os.path.join(
                    chat_directory, "chat_trunecated.json")
            else:
                chat_address = os.path.join(chat_directory, "chat.json")

            probing_questions_address = os.path.join(
                chat_directory, "probing_questions", "probing_questions.json")

            result_save_address = os.path.join(
                "results", chat_size, dir)

            os.makedirs(result_save_address, exist_ok=True)

            answer_generation(probing_questions_address=probing_questions_address,
                              evaluation_type=evaluation_type,
                              chat_address=chat_address,
                              chat_size=chat_size,
                              gpt_llm=gpt_llm,
                              qwen_llm=qwen_llm,
                              model=model,
                              result_save_address=result_save_address,
                              result_save_file_name=result_save_file_name,
                              model_config=model_config,
                              retrieval_config=retrieval_config)
    else:
        def worker(index):
            print(
                f"===================== RUNNING DIRECTORY {index+1} =====================")
            dir = dirs[index]
            chat_directory = os.path.join(input_directory, dir)

            if os.path.exists(os.path.join(chat_directory, "chat_trunecated.json")):
                chat_address = os.path.join(
                    chat_directory, "chat_trunecated.json")
            else:
                chat_address = os.path.join(chat_directory, "chat.json")

            probing_questions_address = os.path.join(
                chat_directory, "probing_questions", "probing_questions.json"
            )

            result_save_address = os.path.join("results", chat_size, dir)
            os.makedirs(result_save_address, exist_ok=True)

            return answer_generation(
                probing_questions_address=probing_questions_address,
                evaluation_type=evaluation_type,
                chat_address=chat_address,
                chat_size=chat_size,
                gpt_llm=gpt_llm,
                qwen_llm=qwen_llm,
                model=model,
                result_save_address=result_save_address,
                result_save_file_name=result_save_file_name,
                model_config=model_config,
                retrieval_config=retrieval_config
            )

        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(worker, index)
                       for index in range(start_index, end_index)]

            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Job failed with error: {e}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Process answer generation parameters")

    parser.add_argument("--qwen_model_url", type=str,
                        required=True, help="URL of the LLM server")
    parser.add_argument("--qwen_model_name", type=str,
                        required=True, help="Directory of the LLM")
    parser.add_argument("--qwen_api_key", type=str, required=True,
                        help="API key for authentication")

    parser.add_argument("--reader_model_url", type=str,
                        required=True, help="URL of the LLM server")
    parser.add_argument("--reader_model_name", type=str,
                        required=True, help="Directory of the LLM")
    parser.add_argument("--reader_model_api_key", type=str, required=True,
                        help="API key for authentication")
    
    parser.add_argument("--gpt_api_key", type=str, required=True,
                        help="API key for authentication")
    
    parser.add_argument("--input_directory", type=str, required=True,
                        help="Directory containing chats")
    parser.add_argument("--chat_size", type=str,
                        required=True, help="Size of chat")
    parser.add_argument("--evaluation_type", type=str, choices=["rag", "long-context", "kg"],
                        required=True, help="Type of evaluation: rag, long-context, or kg")
    parser.add_argument("--result_save_file_name", type=str,
                        required=True, help="Name of the file to save")
    parser.add_argument("--start_index", type=int,
                        required=True, help="Starting index")
    parser.add_argument("--end_index", type=int,
                        required=True, help="Ending index")
    parser.add_argument("--num_threads", type=int,
                        required=True, help="Threads num")

    parser.add_argument("--temperature", type=float, default=0,
                        required=False, help="Temperature of the LLM")
    parser.add_argument("--api_key", type=str,
                        required=False, help="api key")
    parser.add_argument("--request_timeout", type=int, default=60,
                        required=False, help="Rquest timeout of the LLM")
    parser.add_argument("--model_name", type=str,
                        required=False, help="LLM name")
    parser.add_argument("--model_provider", type=str,
                        required=False, help="Model provider")
    parser.add_argument("--max_tokens", type=int,
                        required=False, help="LLM max tokens")
    parser.add_argument("--sleep_time", type=int,
                        required=False, help="LLM sleep time")

    parser.add_argument("--retrieval_method", type=str,
                        required=False, help="Retriever chunk level", choices=["kv", "light", "pair_chunk", "turn_chunk"])
    parser.add_argument("--retriever", type=str,
                        required=False, help="Retriever type", choices=["bm25", "splade", "e5", "dense", "hybrid"])
    parser.add_argument("--k", type=int,
                        required=False, help="Top k")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    gpt_api_key = args.gpt_api_key
    gpt_llm_obj = BuildLLm(model_url=None, 
                           model_name="gpt-4.1-mini",
                           api_key=gpt_api_key,
                           temperature=0)
    gpt_llm = gpt_llm_obj.build_llm()

    english_only_regex = "[\\u0000-\\u2E7F]+"
    qwen_awq_32_llm_obj = BuildLLm(model_url=args.qwen_model_url,
                                   model_name=args.qwen_model_name,
                                   api_key=args.qwen_api_key,
                                   temperature=0,
                                   extra_body={"guided_regex": english_only_regex})
    qwen_llm = qwen_awq_32_llm_obj.build_llm()

    reader_llm_obj = BuildLLm(model_url=args.reader_model_url,
                                   model_name=args.reader_model_name,
                                   api_key=args.reader_model_api_key,
                                   temperature=0)
    reader_llm = reader_llm_obj.build_llm()
    
    model_config = {}
    retrieval_config = {}

    if args.evaluation_type == "long-context":
        model_config = {
            "temperature": args.temperature,
            "api_key": args.api_key,
            "request_timeout": args.request_timeout,
            "model_name": args.model_name,
            "model_provider": args.model_provider,
            "max_tokens": args.max_tokens,
            "sleep_time": args.sleep_time
        }
    else:
        retrieval_config = {
            "retrieval_method": args.retrieval_method,
            "retriever": args.retriever,
            "k": args.k
        }

    start = time.time()
    
    model_config = {
            "temperature": args.temperature,
            "api_key": args.api_key,
            "request_timeout": args.request_timeout,
            "model_name": args.model_name,
            "model_provider": args.model_provider,
            "max_tokens": args.max_tokens,
            "sleep_time": args.sleep_time
        }
    
    batch_run_answer_generation(input_directory=args.input_directory,
                                chat_size=args.chat_size,
                                gpt_llm=gpt_llm,
                                qwen_llm=qwen_llm,
                                model=reader_llm,
                                evaluation_type=args.evaluation_type,
                                result_save_file_name=args.result_save_file_name,
                                start_index=args.start_index,
                                end_index=args.end_index,
                                num_threads=args.num_threads,
                                model_config=model_config,
                                retrieval_config=retrieval_config)

    end = time.time()

    elapsed = int(end - start)
    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60

    print(f"Elapsed time: {hours:02}:{minutes:02}:{seconds:02}")
