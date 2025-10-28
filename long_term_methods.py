import tiktoken
from json_repair import repair_json
from langchain.retrievers.document_compressors import LLMChainFilter
from sentence_transformers import CrossEncoder
import json
from typing import List, Tuple, Optional
from pathlib import Path
import torch
import pickle
from functools import lru_cache
import threading
from transformers import AutoTokenizer
from sentence_transformers import SentenceTransformer, SparseEncoder
from qdrant_client import QdrantClient, models as qmodels
from langchain_core.documents import Document
from langchain_community.retrievers import QdrantSparseVectorRetriever
from huggingface_hub import snapshot_download
from langchain.retrievers import EnsembleRetriever
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_aws import ChatBedrockConverse
from langchain.chat_models import init_chat_model
from langchain_core.embeddings import Embeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import AzureChatOpenAI
from langchain_community.retrievers import BM25Retriever
from concurrent.futures import ThreadPoolExecutor, as_completed
import google.generativeai as genai
from prompts import *
from llm import llama_llm
import os
os.environ["HF_HUB_DISABLE_XET"] = "1"


_model_init_lock = threading.RLock()


@lru_cache(maxsize=20)
def _get_st_client(model_name: str, 
                   device: str | None = None):
    
    with _model_init_lock:
        dev = device or ("cuda" if torch.cuda.is_available() else "cpu")
        local_path = Path(f"./models/{model_name}")
        if not local_path.exists():
            local_path.mkdir(parents=True, exist_ok=True)
            snapshot_download(
                repo_id=model_name,
                local_dir=str(local_path),
                local_dir_use_symlinks=False,
            )
        return SentenceTransformer(str(local_path), device=dev)


_first_call_lock = threading.RLock()


def safe_encode(model, 
                texts, 
                **kwargs):
    
    with _first_call_lock:
        return model.encode(texts, **kwargs)


def hf_emb_from_cached_client(model_name: str, 
                              normalize=True, 
                              device: str | None = None):
    
    st = _get_st_client(model_name, device=device)
    return HuggingFaceEmbeddings(
        client=st,
        encode_kwargs={"normalize_embeddings": normalize}
    )


class CachedHFEmbeddings(Embeddings):
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.model = _get_st_client(model_name)

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return safe_encode(self.model, texts, normalize_embeddings=True).tolist()

    def embed_query(self, text: str) -> list[float]:
        return safe_encode(self.model, [text], normalize_embeddings=True)[0].tolist()


class E5Embeddings(HuggingFaceEmbeddings):
    def embed_documents(self, texts):
        texts = [f"passage: {t}" for t in texts]
        return super().embed_documents(texts)

    def embed_query(self, text):
        return super().embed_query(f"query: {text}")


def build_faiss_retriever_e5(model_name: str,
                             texts: list,
                             metas: list,
                             k: int = 5,
                             search_type: str = "similarity"):

    st = _get_st_client(model_name)
    emb = E5Embeddings(client=st, encode_kwargs={"normalize_embeddings": True})
    vs = FAISS.from_texts(texts, emb, metadatas=metas)
    return vs.as_retriever(search_type=search_type, search_kwargs={"k": k})


@lru_cache(maxsize=20)
def _get_splade_client(model_name: str,
                       device: Optional[str] = None) -> SparseEncoder:
    with _model_init_lock:
        if model_name == "naver/splade-cocondenser-ensembledistil":
            local_dir = Path("./models/splade-cocondenser-ensembledistil")
            cfg_file = local_dir / "config.json"

            if not cfg_file.exists():
                local_dir.mkdir(parents=True, exist_ok=True)
                snapshot_download(
                    repo_id=model_name,
                    local_dir=str(local_dir),
                    local_dir_use_symlinks=False,
                )

            return SparseEncoder(str(local_dir))
        else:
            raise ValueError(f"{model_name} is not a supported SPLADE model.")


def _encode_splade_sparse(
    model: SparseEncoder,
    texts: List[str],) -> List[Tuple[List[int], List[float]]]:
    
    with _first_call_lock, torch.inference_mode():
        emb = model.encode(
            texts,
            convert_to_tensor=True,
            convert_to_sparse_tensor=True,
            show_progress_bar=False,
        )

    if emb.layout != torch.sparse_csr:
        emb = emb.to_sparse_csr()

    indptr = emb.crow_indices()
    cols = emb.col_indices()
    vals = emb.values()

    out: List[Tuple[List[int], List[float]]] = []
    for i in range(emb.size(0)):
        start = indptr[i].item()
        end = indptr[i + 1].item()
        row_cols = cols[start:end].cpu().tolist()
        row_vals = vals[start:end].cpu().tolist()
        out.append((row_cols, row_vals))
    return out


def build_splade_retriever(
    texts: List[str],
    metas: List[dict],
    k: int = 5,
    collection_name: str = "splade_v2_sparse",
    vector_name: str = "splade_v2",
    model_name: str = "naver/splade-cocondenser-ensembledistil",
    device: Optional[str] = None,
    client: Optional[QdrantClient] = None,
):
    splade_st = _get_splade_client(model_name, device=device)

    def splade_encoder(text: str) -> Tuple[List[int], List[float]]:
        return _encode_splade_sparse(splade_st, [text])[0]

    client = client or QdrantClient(location=":memory:")
    try:
        client.delete_collection(collection_name)
    except Exception:
        pass

    client.create_collection(
        collection_name=collection_name,
        vectors_config={},
        sparse_vectors_config={
            vector_name: qmodels.SparseVectorParams(
                index=qmodels.SparseIndexParams(on_disk=False)
            )
        },
    )

    retriever = QdrantSparseVectorRetriever(
        client=client,
        collection_name=collection_name,
        sparse_vector_name=vector_name,
        sparse_encoder=splade_encoder,
        k=k,
    )

    docs = [Document(page_content=t, metadata=m) for t, m in zip(texts, metas)]
    retriever.add_documents(docs)
    return retriever


def get_encoder(model_name: str,
                model_type: str,
                api_key: str):

    if model_type == "gpt":
        encoder = tiktoken.encoding_for_model(model_name)

    elif model_type == "other":
        encoder = tiktoken.get_encoding("cl100k_base")

    elif model_type == "gemini":
        class GeminiEncoder:
            def __init__(self, model_name: str, api_key: str):
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel(model_name)

            def encode(self, text: str):
                """Return a dummy token list of the right length."""
                count = self.model.count_tokens(text).total_tokens
                return [0] * count

        return GeminiEncoder(model_name, api_key)

    return encoder


def total_tokens(messages: list,
                 enc) -> int:
    """
      • 4 tokens per message (role + wrappers)
      • len(encode(content)) for the text itself
      • +2 for system priming & assistant reply
    """
    tok = 2
    for message in messages:
        tok += 4 + len(enc.encode(message["content"]))
    return tok


def prune_from_tail(messages: list,
                    max_tokens: int,
                    encoder):

    total_tokens_number = total_tokens(messages, encoder)
    final_messages = []
    if total_tokens_number > max_tokens - 10000:
        tokens_to_remove = max_tokens - 2000
        count = 0
        for index, message in enumerate(reversed(messages)):
            count += total_tokens([message], encoder)
            if count > tokens_to_remove:
                final_messages = messages[-(index+1):]
                if len(final_messages) % 2 == 1:
                    final_messages = final_messages[1:]
                break

        return final_messages

    else:
        return messages


def build_faiss_retriever(model_name: str,
                          search_type: str,
                          texts: list,
                          metas: list,
                          k=5):

    st = _get_st_client(model_name)

    emb = CachedHFEmbeddings(model_name)
    vs = FAISS.from_texts(texts, emb, metadatas=metas)
    return vs.as_retriever(search_type=search_type, search_kwargs={"k": k})


def create_kv_rag_method(messages: list,
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


def create_scratch_pad_chunks(messages: list,
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


def create_chunking(messages: list,
                    chat_size: str,
                    retrieval_method: str,
                    scratchpad_save_address: str,
                    qwen_llm,
                    gpt_llm):

    scratch_pad = ""
    chunks = []
    short_term_chunks = None
    if retrieval_method == "pair_chunk":
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
                                    "metadata": {"batch_number": batch_number+1, "turn_number": turn_number+1, "pair_number": pair_number+1}
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
                                "metadata": {"batch_number": batch_number+1, "turn_number": turn_number+1, "pair_number": pair_number+1}
                            })

    elif retrieval_method == "turn_chunk":
        if chat_size == "10M":
            for plan_number, plan in enumerate(messages):
                for batch_number, batch in enumerate(list(plan.values())[0]):
                    turns = batch['turns']
                    for turn_number, turn in enumerate(turns):
                        text = ""
                        for message in turn:
                            text += f"{message['role'].upper()}: {message['content']} \n\n"

                        chunks.append({
                            "text": text,
                            "metadata": {"batch_number": batch_number, "turn_number": turn_number}
                        })
        else:
            for batch_number, batch in enumerate(messages):
                turns = batch['turns']
                for turn_number, turn in enumerate(turns):
                    text = ""
                    for message in turn:
                        text += f"{message['role'].upper()}: {message['content']} \n\n"

                    chunks.append({
                        "text": text,
                        "metadata": {"batch_number": batch_number, "turn_number": turn_number}
                    })

    elif retrieval_method == "kv":
        chunks = create_kv_rag_method(messages=messages,
                                      chat_size=chat_size,
                                      qwen_llm=qwen_llm,
                                      gpt_llm=gpt_llm)

    elif retrieval_method == "light":
        file_address = os.path.join(
            scratchpad_save_address, "scrach_pad_new.txt")

        if os.path.isfile(file_address):
            with open(file_address, "r") as f:
                scratch_pad = f.read()
        else:
            scratch_pad = create_scratch_pad_chunks(messages=messages,
                                                    chat_size=chat_size,
                                                    qwen_llm=qwen_llm,
                                                    gpt_llm=gpt_llm)

            with open(file_address, "w") as f:
                f.write(scratch_pad)

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
            long_term_chunks = create_kv_rag_method(messages=messages,
                                                    chat_size=chat_size,
                                                    qwen_llm=qwen_llm,
                                                    gpt_llm=gpt_llm)
            long_term_original_texts = [
                c["original_text"] for c in long_term_chunks]
            long_term_texts = [c["text"] for c in long_term_chunks]
            long_term_metas = [c["metadata"] for c in long_term_chunks]

            with open(long_term_chunks_address, "wb") as f:
                pickle.dump(long_term_chunks, f)

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

        chunks = long_term_chunks
        texts = long_term_texts + short_term_texts
        metas = long_term_metas + short_term_metas

    return chunks, short_term_chunks, scratch_pad


def create_retriever(retriever_name: str,
                     texts: list,
                     metas: list,
                     k: int,
                     query: str,
                     saved_retriever):

    temp_saved_retriever = None

    if retriever_name == "bm25":
        if not saved_retriever:
            sparse_retriever = BM25Retriever.from_texts(
                texts, metadatas=metas, k=k)

            result = sparse_retriever.get_relevant_documents(
                query=query, k=k)

            temp_saved_retriever = sparse_retriever

        else:
            result = saved_retriever.get_relevant_documents(
                query=query, k=k)

    elif retriever_name == "splade":
        if not saved_retriever:
            splade_retr = build_splade_retriever(
                texts=texts, metas=metas, k=k)
            result = splade_retr.get_relevant_documents(query=query, k=k)
            temp_saved_retriever = splade_retr
        else:
            result = saved_retriever.get_relevant_documents(
                query=query, k=k)

    elif retriever_name == "e5":
        if not saved_retriever:
            # "intfloat/e5-small-v2"  (fast)
            # "intfloat/e5-base-v2"   (balanced)
            # "intfloat/e5-large-v2"  (highest quality, slower)
            e5_model_name = "intfloat/e5-large-v2"

            e5_retr = build_faiss_retriever_e5(
                model_name=e5_model_name,
                texts=texts,
                metas=metas,
                k=k,
                search_type="similarity"
            )
            result = e5_retr.get_relevant_documents(query=query)
            temp_saved_retriever = e5_retr
        else:
            result = saved_retriever.get_relevant_documents(query=query)

    elif retriever_name == "dense":
        if not saved_retriever:
            contriever_retr = build_faiss_retriever(model_name="BAAI/bge-small-en-v1.5",
                                                    search_type="similarity",
                                                    texts=texts,
                                                    metas=metas,
                                                    k=k)

            result = contriever_retr.get_relevant_documents(query=query)
            temp_saved_retriever = contriever_retr

        else:
            result = saved_retriever.get_relevant_documents(query=query)

    elif retriever_name == "hybrid":
        if not saved_retriever:
            bge_large_retr = build_faiss_retriever("BAAI/bge-large-en-v1.5",
                                                   search_type="similarity",
                                                   texts=texts,
                                                   metas=metas,
                                                   k=k)

            sparse_retriever = BM25Retriever.from_texts(
                texts, metadatas=metas, k=k)

            hybrid_retriever = EnsembleRetriever(
                retrievers=[sparse_retriever, bge_large_retr],
                weights=[0.3, 0.7],
            )

            result = hybrid_retriever.get_relevant_documents(query=query)

            temp_saved_retriever = hybrid_retriever

        else:
            result = saved_retriever.get_relevant_documents(query=query)

    return result, temp_saved_retriever


def handling_context(retrieval_method: str,
                     result: list,
                     chunks: list,
                     short_term_chunks: list,
                     original_texts: list,
                     scratch_pad: str,
                     saved_retriever,
                     query,
                     qwen_llm):

    reader_max_tokens = 29000
    context = ""
    if retrieval_method == "kv":
        final_results = []
        for doc in result:
            id = doc.metadata["id"]
            for obj in original_texts:
                if obj["id"] == id:

                    final_results.append({
                        "text": obj['text']
                    })

        for document in final_results:
            if len(context + document['text']) // 3.5 < reader_max_tokens:
                context += document['text']

    elif retrieval_method == "light":
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
            embedding = CachedHFEmbeddings("BAAI/bge-large-en-v1.5")
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

    else:
        for document in result:
            page_content = document.page_content
            if len(context + page_content) // 3.5 < reader_max_tokens:
                context += page_content

    return context


def probing_question_evaluation(query: str,
                                chat_directory: str,
                                chat_address: str,
                                chat_size: str,
                                evaluation_type: str,
                                gpt_llm,
                                qwen_llm,
                                model=None,
                                model_config: object = None,
                                saved_messages: list = None,
                                retrieval_config: object = None,
                                saved_retriever=None,
                                chunks=None,
                                short_term_chunks=None,
                                current_graph=None,
                                scratch_pad=None) -> None:

    chat_address = chat_address
    with open(chat_address, 'r') as file:
        data = json.load(file)

    if evaluation_type == "long-context":
        model_name = model_config["model_name"]
        model_provider = model_config["model_provider"]
        max_tokens = model_config["max_tokens"]
        temperature = model_config["temperature"]
        api_key = model_config["api_key"]
        request_timeout = model_config["request_timeout"]
        if not model:
            if model_provider == "bedrock_converse":
                model = ChatBedrockConverse(model_id="us.meta.llama4-maverick-17b-instruct-v1:0",
                                            temperature=temperature)
            else:
                model = init_chat_model(model=model_name,
                                        model_provider=model_provider,
                                        temperature=temperature,
                                        api_key=api_key,
                                        timeout=request_timeout)

        if saved_messages:
            messages = saved_messages
        else:
            messages = []
            if chat_size == "10M":
                for plan_number, plan in enumerate(data):
                    for batch_number, batch in enumerate(list(plan.values())[0]):
                        turns = batch['turns']
                        for turn in turns:
                            for message in turn:
                                messages.append({
                                    "role": message["role"],
                                    "content": message["content"]
                                })
            else:
                for batch in data:
                    turns = batch['turns']
                    for turn in turns:
                        for message in turn:
                            messages.append({
                                "role": message["role"],
                                "content": message["content"]
                            })

            if "gemini" in model_name:
                model_type = "gemini"
            else:
                model_type = "other"
            encoder = get_encoder(model_name=model_name,
                                  model_type=model_type,
                                  api_key=api_key)

            messages = prune_from_tail(
                messages=messages, max_tokens=max_tokens, encoder=encoder)

        messages.append({
            "role": "user",
            "content": f"""
            NOTE: Only provide the answer without any explanations. 
            Question: {query}"""
        })

        response = model.invoke(messages).content

        return response, messages[:-1]

    elif evaluation_type == "rag":
        retrieval_method = retrieval_config["retrieval_method"]
        retriever = retrieval_config['retriever']
        k = retrieval_config['k']

        if not saved_retriever:
            chunks = []
            scratch_pad = ""
            chunks, short_term_chunks, scratch_pad = create_chunking(messages=data,
                                                                     chat_size=chat_size,
                                                                     retrieval_method=retrieval_method,
                                                                     scratchpad_save_address=chat_directory,
                                                                     qwen_llm=qwen_llm,
                                                                     gpt_llm=gpt_llm)

        original_texts = []
        if retrieval_method == "kv":
            original_texts = [c["original_text"] for c in chunks]

        texts = [c["text"] for c in chunks]
        metas = [c["metadata"] for c in chunks]

        temp_saved_retriever = None

        result, temp_saved_retriever = create_retriever(retriever_name=retriever,
                                                        texts=texts,
                                                        metas=metas,
                                                        k=k,
                                                        query=query,
                                                        saved_retriever=saved_retriever)

        context = handling_context(retrieval_method=retrieval_method,
                                   result=result,
                                   chunks=chunks,
                                   short_term_chunks=short_term_chunks,
                                   original_texts=original_texts,
                                   scratch_pad=scratch_pad,
                                   saved_retriever=saved_retriever,
                                   query=query,
                                   qwen_llm=qwen_llm)

        prompt = answer_generation_for_rag\
            .replace("<context>", context)\
            .replace("<question>", query)

        response = model.invoke(prompt).content

        return response, temp_saved_retriever, chunks, short_term_chunks, scratch_pad
