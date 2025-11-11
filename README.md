# Codes and data for the paper: [**BEYOND A MILLION TOKENS: BENCHMARKING AND ENHANCING LONG-TERM MEMORY IN LLMS**]()

Evaluating the abilities of large language models (LLMs) for tasks that require long-term memory and thus long-context reasoning, for example in conversational settings, is hampered by the existing benchmarks, which often lack narrative coherence, cover narrow domains, and only test simple recall-oriented tasks. This paper introduces a comprehensive solution to these challenges. First, we present a novel framework for automatically generating long (up to 10M tokens), coherent, and topically diverse conversations, accompanied by probing questions targeting a wide range of memory abilities. From this, we construct BEAM, a new benchmark comprising 100 conversations and 2,000 validated questions. Second, to enhance model performance, we propose LIGHT–a framework inspired by human cognition that equips LLMs with three complementary memory systems: a long-term episodic memory, a short-term working memory, and a scratchpad for accumulating salient facts. Our experiments on BEAM reveal that even LLMs with 1M token context windows (with and without retrieval-augmentation) struggle as dialogues lengthen. In contrast, LIGHT consistently improves performance across various models, achieving an average improvement of 3.5%–12.69% over the strongest baselines, depending on the backbone LLM. An ablation study further confirms the contribution of each memory component.

## 🧠 BEAM Description
BEAM is a comprehensive dataset for evaluating long-term memory in language models. It contains multi-scale conversations (128K, 500K, 1M, and 10M tokens) spanning diverse domains, including general, coding, and mathematical topics, and is designed to assess ten distinct memory abilities. To evaluate LLMs on these abilities, we generate a set of probing questions for each conversation.

### 📊 Dataset Statistics
BEAM consists of 100 conversations distributed as follows:
- **128K**: 20 chats  
- **500K**: 35 chats  
- **1M**: 35 chats  
- **10M**: 10 chats  

| **Chat Size** | **# User Messages** | **# Assistant Messages** | **# Answer Assistant Questions** | **# Follow-up Questions** | **# Turns** |
|:-------------:|:-------------------:|:------------------------:|:-------------------------------:|:-------------------------:|:------------:|
| 128K | 144 | 144 | 27 | 216 | 107 |
| 500K | 544 | 544 | 79 | 51 | 416 |
| 1M | 1,067 | 1,067 | 105 | 120 | 842 |
| 10M | 10,435 | 10,435 | 1,151 | 1,528 | 7,757 |

*Statistics of the BEAM dataset. Reported values are averages per chat in each chat size. “# User Messages” and “# Assistant Messages” denote the average number of utterances from each side. “# Answer Assistant Questions” indicates how often the assistant posed a question that the user answered. “# Follow-up Questions” counts user follow-ups, and “# Turns” refers to the total number of dialogue turns.*

### 🧩 Probing Questions Types
1. **Abstention**: Evaluates whether a model withholds answers when evidence is missing
2. **Contradiction Resolution**: Tests the capacity to detect and reconcile inconsistent statements across widely separated turns, maintaining global coherence
3. **Event Ordering**: Assesses whether a model can recognize and reconstruct the sequence of evolving information in the dialogue
4. **Information Extraction**: Measures recall of entities and factual details in long histories
5. **Instruction Following**: Examines sustained adherence to user-specified constraints over long contexts
6. **Knowledge Update**: Evaluates revising stored facts as new ones appear
7. **Multi-Session Reasoning**: Probes inference that integrates evidence across multiple, non-adjacent dialogue segments
8. **Preference Following**: Captures personalized responses that adapt to evolving preferences
9. **Summarization**: Assesses the ability to abstract and compress dialogue content
10. **Temporal Reasoning**: Tests reasoning about explicit and implicit time relations

## ⚙️ LIGHT Framework

**LIGHT** is a **cognitively inspired memory-augmented framework** designed to enhance long-term memory in large language models.

It draws inspiration from human memory systems and integrates **three complementary components** that work together during inference:

1. **Episodic Memory** – A long-term memory index that retrieves relevant information across extended contexts.  
2. **Working Memory** – A short-term buffer that retains the most recent dialogue turns, enabling continuity and contextual relevance.  
3. **Scratchpad** – An iteratively compressed semantic layer that tracks salient facts, user instructions, and contextual updates after each turn.

At inference time, LIGHT retrieves and integrates information from all three memory systems, enabling the model to produce **more grounded, coherent, and contextually consistent responses** even in conversations spanning millions of tokens.

### 🔬 Evaluation Results
LIGHT demonstrates consistent improvements across all evaluated models on the BEAM benchmark, achieving **3.5%–12.7% higher accuracy** on probing questions compared to the strongest baselines.  
An ablation study confirms that each component—episodic retrieval, working memory, and scratchpad—contributes complementary benefits to overall performance.

### 🧩 How to Use LIGHT
The detailed implementation of each memory component—episodic memory, working memory, and scratchpad—can be found in:
`
src/answer_probing_questions/light.py
`

## 📦 Dataset Access and Download

The BEAM dataset is publicly available on the [Hugging Face Hub](https://huggingface.co/datasets/Mohammadta/BEAM) and also included within this repository.

### 🔗 Hugging Face Links
- **BEAM (128K, 500K, 1M chats)** – [https://huggingface.co/datasets/Mohammadta/BEAM](https://huggingface.co/datasets/Mohammadta/BEAM)  
- **BEAM-10M (10M-token chats)** – [https://huggingface.co/datasets/Mohammadta/BEAM-10M](https://huggingface.co/datasets/Mohammadta/BEAM-10M)

Each dataset contains multi-turn conversations and corresponding metadata required for memory-ability evaluation.

---

### 🗂 Local Copy
A copy of the chat data is also provided in the repository under: /chats/
---

### ⚙️ Automatic Download and Pre-processing
To simplify setup, we provide a script that automatically downloads and formats the dataset for use with the provided codebase.

Run the following command from the root directory:
```bash
python src/beam/download_dataset.py
```
After running it, the dataset will be ready to use for model evaluation or reproduction of the results from the paper.

## ⚙️ Installation

To install all required dependencies, run:

```bash
pip install -r requirements.txt
```

This will install all necessary libraries for dataset generation, probing question creation, answer generation, and evaluation.

---

## 🚀 Usage Guide

### 1️⃣ Dataset Generation

The topics of the chats are provided in the `topics/` directory.  
To recreate the dataset (as provided in this repository), follow these steps:

#### Step 1: Configure LLMs
Define your model configurations — including model URLs, names, and API keys — inside:
```
src/llms_config.json
```

#### Step 2: Run the Pipeline
The dataset generation process is divided into **three stages**, executed with `run_pipeline.sh`.

Each command follows this format:

```bash
bash src/beam/run_pipeline.sh [llm_url] [llm_name] [llm_api_key] [stage] [start_index] [end_index] [chat_directory] [chat_size]
```

For example:

```bash
# 1. Create conversation plans
bash src/beam/run_pipeline.sh http://localhost:8000 llama3 my_api_key plan 0 10 chats/1M 1M

# 2. Create user questions
bash src/beam/run_pipeline.sh http://localhost:8000 llama3 my_api_key question 0 10 chats/1M 1M

# 3. Create assistant answers
bash src/beam/run_pipeline.sh http://localhost:8000 llama3 my_api_key answer 0 10 chats/1M 1M
```

---

### 2️⃣ Create Probing Questions
After generating the chats, the next step is to create probing questions for each conversation.

For 128K, 500K, and 1M chat sizes, run the function `create_probing_questions` inside:
`
src/beam/main.py
`

For 10M chat size, run the function `ten_m_create_probing_questions` inside:
`
src/beam/ten_milion_pipeline.py
`

These functions automatically generate probing questions that evaluate ten distinct memory abilities for each conversation.

---


### ⚠️ **Build Your Own Multi-Turn Dialogues**

You can **build your own multi-turn conversational datasets** of any size — including **128K, 500K, 1M, 10M tokens**, or even longer.

To do this:

1. Prepare your own **chat seed information**, similar to the examples in the `topics/` directory.  
2. Define your **LLM configurations** in `src/llms_config.json`.  
3. Run the same **three-stage pipeline** described above (`plan → question → answer`).  
4. Create probing questions using the appropriate function (`create_probing_questions` and `ten_m_create_probing_questions`).
5. Design evaluation rubrics

This process automatically generates long, coherent, multi-domain dialogues ready for probing and evaluation.

---

### 3️⃣ Generate Answers to Probing Questions

After the dataset and probing questions are ready, generate answers using:

```bash
bash src/model_inference/answer_generation.sh
```

Before running, you must edit the environment variables inside the file answer_generation.sh to match your experimental setup.
- **For long-context LLMs:**  
  Set `EVAL_TYPE="long-context"`  

- **For the RAG baseline:**  
  Set `EVAL_TYPE="rag"`, `RETRIEVAL_METHOD="pair_chunk"` and `RETRIEVER="dense"`  

- **For LIGHT (our proposed method):**  
  Set `EVAL_TYPE="rag"` and `RETRIEVAL_METHOD="light"` 

---

### 4️⃣ Evaluate Generated Answers

To evaluate the generated answers against reference probing questions, run:

```bash
python -m src.evaluation.run_evaluation \
    --input_directory [results directory e.g. results/1M] \
    --chat_size [chat size e.g. 1M] \
    --start_index [start index] \
    --end_index [end index] \
    --max_workers [num workers] \
    --allowed_result_files [list of result files to evaluate]
```

This script uses an LLM-as-a-judge model to score each generated answer against the corresponding probing question.
The judging LLM assigns a numerical score for each memory ability category.
All evaluation scores are automatically saved in the specified results directory for later analysis and reporting.

---

### 5️⃣ Generate and Save Reports

To aggregate and export evaluation results into a structured Excel file, run:

```bash
python -m src.evaluation.report_results.py \
    --evaluation_directory [evaluation directory e.g. results/1M/] \
    --row_names [evaluation file names to display] \
    --output_filename [output filename]
```

This script combines evaluation results across models and probing categories and produces a `.xlsx` report for analysis and comparison.

---

> 💡 **Tip:** The pipeline is fully modular — you can independently run dataset creation, question generation, answer generation, and evaluation, depending on your specific experimental needs.


# 📝 References

If you find this work helpful or use the code or dataset, please cite the following paper:

[Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs](https://arxiv.org/abs/2510.27246)

```
@misc{tavakoli2025milliontokensbenchmarkingenhancing,
      title={Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs}, 
      author={Mohammad Tavakoli and Alireza Salemi and Carrie Ye and Mohamed Abdalla and Hamed Zamani and J Ross Mitchell},
      year={2025},
      eprint={2510.27246},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.27246}, 
}
```