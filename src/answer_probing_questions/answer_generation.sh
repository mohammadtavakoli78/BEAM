#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

cd "$SCRIPT_DIR/../.."

# === Environment variables ===
export GPT_API_KEY=""

export QWEN_MODEL_URL=""
export QWEN_MODEL_NAME=""
export QWEN_API_KEY=""

export READER_MODEL_URL=""
export READER_MODEL_NAME=""
export READER_MODEL_API_KEY=""

export INPUT_DIR=""
export CHAT_SIZE=""
export EVAL_TYPE=""             # rag | long-context
export RESULT_FILE=""

export START_IDX=
export END_IDX=
export NUM_THREADS=

# Optional LLM configs (used if evaluation_type=long-context)
export TEMPERATURE=
export API_KEY=""
export REQUEST_TIMEOUT=
export MODEL_NAME=""
export MODEL_PROVIDER="" # openai | google_genai | bedrock_converse | ...
export MAX_TOKENS=
export SLEEP_TIME=

# Optional retrieval configs (used if evaluation_type=rag)
export RETRIEVAL_METHOD="" # kv | light | pair_chunk | turn_chunk
export RETRIEVER="" # bm25 | splade | e5 | dense | hybrid
export TOP_K= 

# === Run Python ===
python -m src.answer_probing_questions.answer_generation \
  --qwen_model_url "$QWEN_MODEL_URL" \
  --qwen_model_name "$QWEN_MODEL_NAME" \
  --qwen_api_key "$QWEN_API_KEY" \
  --reader_model_url "$READER_MODEL_URL" \
  --reader_model_name "$READER_MODEL_NAME" \
  --reader_model_api_key "$READER_MODEL_API_KEY" \
  --gpt_api_key "$GPT_API_KEY" \
  --input_directory "$INPUT_DIR" \
  --chat_size "$CHAT_SIZE" \
  --evaluation_type "$EVAL_TYPE" \
  --result_save_file_name "$RESULT_FILE" \
  --start_index "$START_IDX" \
  --end_index "$END_IDX" \
  --num_threads "$NUM_THREADS" \
  --temperature "$TEMPERATURE" \
  --api_key "$API_KEY" \
  --request_timeout "$REQUEST_TIMEOUT" \
  --model_name "$MODEL_NAME" \
  --model_provider "$MODEL_PROVIDER" \
  --max_tokens "$MAX_TOKENS" \
  --sleep_time "$SLEEP_TIME" \
  --retrieval_method "$RETRIEVAL_METHOD" \
  --retriever "$RETRIEVER" \
  --k "$TOP_K"
