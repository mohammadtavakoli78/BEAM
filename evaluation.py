import os
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import nltk
from rouge_score import rouge_scorer
from sentence_transformers import SentenceTransformer, util
import numpy as np
import threading
from scipy.stats import kendalltau
from typing import List, Tuple
import re
import json
from json_repair import repair_json

from prompts import *
from llm import *

_models = {}
_models_lock = threading.Lock()


def get_or_create_model(model_name: str):
    """Thread-safe model getter/creator"""
    with _models_lock:
        if model_name not in _models:
            _models[model_name] = SentenceTransformer(model_name)
    return _models[model_name]


def initialize_models():
    """Initialize all required models before threading"""
    model_names = [
        "all-MiniLM-L6-v2",
        "BAAI/bge-large-en-v1.5",
        "BAAI/bge-base-en-v1.5"
    ]

    for model_name in model_names:
        print(f"Initializing model: {model_name}")
        get_or_create_model(model_name)
    print("All models initialized successfully")


nltk.download("punkt", quiet=True)
nltk.download('punkt_tab')

# **************** Helper functions ****************


def compute_bleu(reference: str,
                 candidate: str,
                 weights=(0.25, 0.25, 0.25, 0.25)) -> float:
    """
    Computes BLEU-n (defaults to BLEU-4) for a single reference–candidate pair.
    `weights` can be set to (0.5, 0.5) for BLEU-2, etc.
    """

    ref_tokens = nltk.word_tokenize(reference.lower())
    cand_tokens = nltk.word_tokenize(candidate.lower())
    smoothie = SmoothingFunction().method4        # helps when sentences are short
    return sentence_bleu([ref_tokens], cand_tokens,
                         weights=weights,
                         smoothing_function=smoothie)


def compute_rouge(reference: str,
                  candidate: str) -> dict:
    """
    Returns a dict: {"rouge1": f1, "rouge2": f1, "rougeL": f1}
    (F1 variant of ROUGE, common in generation tasks).
    """

    _ro_scorer = rouge_scorer.RougeScorer(
        ["rouge1", "rouge2", "rougeL"], use_stemmer=True)

    scores = _ro_scorer.score(reference, candidate)
    return {k: v.fmeasure for k, v in scores.items()}


def compute_semantic_similarity(reference: str,
                                candidate: str) -> float:
    """
    Cosine similarity in [-1, 1] (practically 0-1 for this model).
    """

    _sem_model = get_or_create_model("all-MiniLM-L6-v2")

    embeddings = _sem_model.encode(
        [reference, candidate], normalize_embeddings=True)
    return float(util.cos_sim(embeddings[0], embeddings[1]))


def extract_facts(paragraph: str,
                  question: str,
                  model):

    prompt = break_paragraph_to_facts_detailed_prompt.\
        replace("<question>", question).\
        replace("<input_text>", paragraph)

    response = model.invoke(prompt).content.split("\n")

    return response


def llm_equivalence(first_paragraph: str,
                    second_paragraph: str,
                    llm) -> bool:

    system_msg = {
        "role": "system",
        "content": """
            You are a binary classifier.
            If the TWO snippets describe the SAME event/fact, reply **YES**
            Otherwise reply **NO**. No extra words.
            DO NOT provide any exaplanation.
        """
    }
    user_msg = {
        "role": "user",
        "content": f"""First snippet: {first_paragraph} \n
                       Second snippet: {second_paragraph}
                    """
    }

    messages = [system_msg, user_msg]
    response = llm.invoke(messages).content.lower()

    if "yes" in response:
        result = True
    else:
        result = False

    return result


def align_with_llm(reference: List[str],
        system: List[str],
        llm) -> Tuple[List[str], List[str]]:

    used = set()
    system_out = []

    for s in system:
        matched_index = None
        for index, r in enumerate(reference):
            if index in used:
                continue

            if llm_equivalence(first_paragraph=r,
                               second_paragraph=s,
                               llm=llm):

                matched_index = index
                break

        if matched_index is not None:
            system_out.append(reference[matched_index])
            used.add(matched_index)
        else:
            system_out.append(s)

    return reference, system_out


def semantic_fact_precision_recall_f1(pred_facts: list,
                                      ref_facts: list,
                                      align_type: str,
                                      llm,
                                      threshold=0.7):

    if align_type == "semantic":
        model = get_or_create_model("BAAI/bge-large-en-v1.5")

        if isinstance(pred_facts, str):
            pred_facts = [pred_facts]
        if isinstance(ref_facts, str):
            ref_facts = [ref_facts]
        if not pred_facts or not ref_facts:
            return 0.0, 0.0, 0.0

        pred_embeddings = model.encode(pred_facts, convert_to_tensor=True)
        ref_embeddings = model.encode(ref_facts, convert_to_tensor=True)

        matches = 0
        matched_ref = set()

        for p_embed in pred_embeddings:
            if p_embed.ndim == 1:
                p_embed = p_embed.unsqueeze(0)
            elif p_embed.ndim != 2 or p_embed.shape[0] != 1:
                raise ValueError(
                    f"Unexpected shape for p_embed: {p_embed.shape}")

            sims = util.cos_sim(p_embed, ref_embeddings).squeeze(0)
            best_idx = np.argmax(sims.cpu().numpy())
            if sims[best_idx] >= threshold and best_idx not in matched_ref:
                matches += 1
                matched_ref.add(best_idx)

    elif align_type == "llm":
        reference, system_out = align_with_llm(reference=ref_facts,
                                               system=pred_facts,
                                               llm=llm)

        matches = 0
        for s in system_out:
            if s in reference:
                matches += 1

    precision = matches / len(pred_facts)
    recall = matches / len(ref_facts)
    f1 = 2 * precision * recall / \
        (precision + recall) if (precision + recall) else 0.0

    return precision, recall, f1


def evaluate_fact_level(question: str,
                        paragraph_pred: str,
                        paragraph_ref: str,
                        align_type: str,
                        model):

    pred_facts = extract_facts(paragraph=paragraph_pred,
                               question=question,
                               model=model)

    ref_facts = extract_facts(paragraph=paragraph_ref,
                              question=question,
                              model=model)

    print("Predicted facts: \n", pred_facts, "\n\n")
    print("Reference facts: \n", ref_facts)

    return semantic_fact_precision_recall_f1(pred_facts=pred_facts,
                                             ref_facts=ref_facts,
                                             align_type=align_type,
                                             llm=model)


def semantic_align(reference: List[str], 
                   system: List[str], 
                   thr: float = 0.65) -> Tuple[List[str], List[str]]:
    """
    Replace each system item by its matched gold item if cosine ≥ thr.
    Ensures 1-to-1 mapping (first match wins).
    """

    embedding_model = get_or_create_model("all-MiniLM-L6-v2")

    reference_embbedding = embedding_model.encode(
        reference,   normalize_embeddings=True)
    system_embedding = embedding_model.encode(
        system, normalize_embeddings=True)

    used_reference = set()
    system_canon = []

    for system_vec, system_txt in zip(system_embedding, system):
        sims = util.cos_sim(system_vec, reference_embbedding)[0].cpu().numpy()
        best = int(np.argmax(sims))
        if sims[best] >= thr and best not in used_reference:
            system_canon.append(reference[best])
            used_reference.add(best)
        else:
            system_canon.append(system_txt)
    return reference, system_canon


def event_ordering_score(reference_list: List[str],
                         system_list: List[str],
                         align_type: str,
                         llm,
                         thr: float = 0.65) -> dict:

    # -------- Canonicalise system list semantically --------
    if align_type == "semantic":
        reference_canon, system_canon = semantic_align(reference=reference_list,
                                                       system=system_list,
                                                       thr=thr)
    elif align_type == "llm":
        reference_canon, system_canon = align_with_llm(reference=reference_list,
                                                       system=system_list,
                                                       llm=llm)

    tp = len(set(reference_canon) & set(system_canon))
    fp = len([x for x in system_canon if x not in reference_canon])
    fn = len([x for x in reference_canon if x not in system_canon])

    precision = tp / (tp + fp) if tp + fp else 0
    recall = tp / (tp + fn) if tp + fn else 0
    f1 = 2*precision*recall/(precision+recall) if precision+recall else 0

    union = list(dict.fromkeys(reference_canon + system_canon))
    tie_rank = len(union) + 1

    def to_rank(seq):
        r = {item: i+1 for i, item in enumerate(seq)}
        return [r.get(u, tie_rank) for u in union]

    tau_b, p_value = kendalltau(to_rank(reference_canon),
                                to_rank(system_canon),
                                variant="b", method="auto")
    tau_b_norm = (tau_b + 1) / 2 if tau_b is not None else 0

    final_score = tau_b_norm * f1
    return dict(precision=precision, recall=recall, f1=f1,
                tau_norm=tau_b_norm, final_score=final_score)


def parse_json_response(response: str):
    response = response.strip()

    if response.startswith("```"):
        match = re.search(
            r"```(?:json)?\s*(\[.*\]|\{.*\})\s*```", response, re.DOTALL)
        if match:
            response = match.group(1).strip()

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        pass

    match = re.search(r'(\{.*?\}|\[.*?\])', response, re.DOTALL)
    if match:
        json_part = match.group(1)
        try:
            return json.loads(json_part)
        except Exception as e:
            raise ValueError(
                f"Found possible JSON but failed to parse it: {e}")

    raise ValueError("No valid JSON found in response.")


# **************** Metrics ****************

def evaluate_abstention(rubric: list,
                        llm_response: str,
                        probing_question: str,
                        model):

    llm_judge_responses = []
    score = 0
    for item in rubric:
        prompt = unified_llm_judge_base_prompt.\
            replace("<rubric_item>", item).\
            replace("<llm_response>", llm_response)

        response = model.invoke(prompt).content.strip()
        try:
            response = parse_json_response(response=response)
        except:
            response = json.loads(repair_json(response))

        score += int(response['score'])
        llm_judge_responses.append(response)

    llm_judge_score = score / len(rubric)

    return dict(
        llm_judge_score=llm_judge_score,
        llm_judge_responses=llm_judge_responses
    )


def evaluate_contradiction_resolution(rubric: list,
                                      llm_response: str,
                                      probing_question: str,
                                      model):
    llm_judge_responses = []
    score = 0
    for item in rubric:
        prompt = unified_llm_judge_base_prompt.\
            replace("<rubric_item>", item).\
            replace("<llm_response>", llm_response)

        response = model.invoke(prompt).content.strip()
        try:
            response = parse_json_response(response=response)
        except:
            response = json.loads(repair_json(response))

        score += int(response['score'])
        llm_judge_responses.append(response)

    llm_judge_score = score / len(rubric)

    return dict(
        llm_judge_score=llm_judge_score,
        llm_judge_responses=llm_judge_responses
    )


def evaluate_event_ordering(rubric: list,
                            llm_response: str,
                            probing_question: str,
                            model):

    system_list = extract_facts(paragraph=llm_response,
                                question=probing_question,
                                model=model)

    system_list = llm_response.split("\n")

    score = event_ordering_score(reference_list=rubric,
                                 system_list=system_list,
                                 align_type="llm",
                                 llm=model)

    llm_judge_responses = []
    llm_judge_score = 0
    for item in rubric:
        prompt = unified_llm_judge_base_prompt.\
            replace("<rubric_item>", item).\
            replace("<llm_response>", llm_response)

        response = model.invoke(prompt).content.strip()
        try:
            response = parse_json_response(response=response)
        except:
            response = json.loads(repair_json(response))

        llm_judge_score += float(response['score'])
        llm_judge_responses.append(response)

    llm_judge_score = llm_judge_score / len(rubric)

    score["llm_judge_score"] = llm_judge_score
    score["llm_judge_responses"] = llm_judge_responses

    return score


def evaluate_information_extraction(rubric: list,
                                    llm_response: str,
                                    probing_question: str,
                                    model):

    llm_judge_responses = []
    score = 0
    for item in rubric:
        prompt = unified_llm_judge_base_prompt.\
            replace("<rubric_item>", item).\
            replace("<llm_response>", llm_response)

        response = model.invoke(prompt).content.strip()
        try:
            response = parse_json_response(response=response)
        except:
            response = json.loads(repair_json(response))

        score += int(response['score'])
        llm_judge_responses.append(response)

    llm_judge_score = score / len(rubric)

    return dict(
        llm_judge_score=llm_judge_score,
        llm_judge_responses=llm_judge_responses
    )


def evaluate_instruction_following(rubric: list,
                                   llm_response: str,
                                   probing_question: str,
                                   model):
    
    llm_judge_responses = []
    score = 0
    for item in rubric:
        prompt = unified_llm_judge_base_prompt.\
            replace("<rubric_item>", item).\
            replace("<llm_response>", llm_response)

        response = model.invoke(prompt).content.strip()
        try:
            response = parse_json_response(response=response)
        except:
            response = json.loads(repair_json(response))

        score += int(response['score'])
        llm_judge_responses.append(response)

    llm_judge_score = score / len(rubric)

    return dict(
        llm_judge_score=llm_judge_score,
        llm_judge_responses=llm_judge_responses
    )


def evaluate_knowledge_update(rubric: list,
                              llm_response: str,
                              probing_question: str,
                              model):
    
    llm_judge_responses = []
    score = 0
    for item in rubric:
        prompt = unified_llm_judge_base_prompt.\
            replace("<rubric_item>", item).\
            replace("<llm_response>", llm_response)

        response = model.invoke(prompt).content.strip()
        try:
            response = parse_json_response(response=response)
        except:
            response = json.loads(repair_json(response))

        score += int(response['score'])
        llm_judge_responses.append(response)

    llm_judge_score = score / len(rubric)

    return dict(
        llm_judge_score=llm_judge_score,
        llm_judge_responses=llm_judge_responses
    )


def evaluate_multi_session_reasoning(rubric: list,
                                     llm_response: str,
                                     probing_question: str,
                                     model):

    llm_judge_responses = []
    score = 0
    for item in rubric:
        prompt = unified_llm_judge_base_prompt.\
            replace("<rubric_item>", item).\
            replace("<llm_response>", llm_response)

        response = model.invoke(prompt).content.strip()
        try:
            response = parse_json_response(response=response)
        except:
            response = json.loads(repair_json(response))

        score += int(response['score'])
        llm_judge_responses.append(response)

    llm_judge_score = score / len(rubric)

    return dict(
        llm_judge_score=llm_judge_score,
        llm_judge_responses=llm_judge_responses
    )


def evaluate_preference_following(rubric: list,
                                  llm_response: str,
                                  probing_question: str,
                                  model):
    
    llm_judge_responses = []
    score = 0
    for item in rubric:
        prompt = unified_llm_judge_base_prompt.\
            replace("<rubric_item>", item).\
            replace("<llm_response>", llm_response)

        response = model.invoke(prompt).content.strip()
        try:
            response = parse_json_response(response=response)
        except:
            response = json.loads(repair_json(response))

        score += int(response['score'])
        llm_judge_responses.append(response)

    llm_judge_score = score / len(rubric)

    return dict(
        llm_judge_score=llm_judge_score,
        llm_judge_responses=llm_judge_responses
    )


def evaluate_summarization(rubric: list,
                           llm_response: str,
                           probing_question: str,
                           model):
    
    llm_judge_responses = []
    score = 0
    for item in rubric:
        prompt = unified_llm_judge_base_prompt.\
            replace("<rubric_item>", item).\
            replace("<llm_response>", llm_response)

        response = model.invoke(prompt).content.strip()
        try:
            response = parse_json_response(response=response)
        except:
            response = json.loads(repair_json(response))

        score += int(response['score'])
        llm_judge_responses.append(response)

    llm_judge_score = score / len(rubric)

    return dict(
        llm_judge_score=llm_judge_score,
        llm_judge_responses=llm_judge_responses
    )


def evaluate_temporal_reasoning(rubric: list,
                                llm_response: str,
                                probing_question: str,
                                model):

    llm_judge_responses = []
    score = 0
    for item in rubric:
        prompt = unified_llm_judge_base_prompt.\
            replace("<rubric_item>", item).\
            replace("<llm_response>", llm_response)

        response = model.invoke(prompt).content.strip()
        try:
            response = parse_json_response(response=response)
        except:
            response = json.loads(repair_json(response))

        score += int(response['score'])
        llm_judge_responses.append(response)

    llm_judge_score = score / len(rubric)

    return dict(
        llm_judge_score=llm_judge_score,
        llm_judge_responses=llm_judge_responses
    )
