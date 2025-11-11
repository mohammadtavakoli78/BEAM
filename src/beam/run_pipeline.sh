#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

cd "$SCRIPT_DIR/../.."

MODEL_URL=$1
MODEL_NAME=$2
API_KEY=$3
GENERATION_STAGE=$4
START_INDEX=$5
END_INDEX=$6
CHATS_DIR=$7
CHAT_SIZE=$8

python -m src.beam.run_pipeline \
  --model_url "$MODEL_URL" \
  --model_name "$MODEL_NAME" \
  --api_key "$API_KEY" \
  --generation_stage "$GENERATION_STAGE" \
  --start_index $START_INDEX \
  --end_index $END_INDEX \
  --chats_dir "$CHATS_DIR" \
  --chat_size "$CHAT_SIZE"
