from langchain_openai import ChatOpenAI
import json
import os


class BuildLLm:
    def __init__(self, model_url, model_name, api_key, temperature, frequency_penalty=None, presence_penalty=None, top_p=None, n=None, extra_body=None):
        self.model_url = model_url
        self.model_name = model_name
        self.api_key = api_key
        self.temperature = temperature
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.llm = None
        self.top_p = top_p
        self.n = n
        self.extra_body = extra_body

    def build_llm(self):
        self.llm = ChatOpenAI(
            model=self.model_name,
            openai_api_key=self.api_key,
            openai_api_base=self.model_url,
            temperature=self.temperature,
            extra_body=self.extra_body
        )

        return self.llm

    def set_paramaters(self, model_url, model_name, api_key, temperature):
        self.model_url = model_url
        self.model_name = model_name
        self.api_key = api_key
        self.temperature = temperature

    def get_llm(self):
        return self.llm


english_only_regex = (
    r"^[\t\n\r -~"           # ASCII printable + whitespace
    r"\u00A0-\u00FF"         # Latin-1 Supplement (× ÷ ± ° etc.)
    r"\u0370-\u03FF"         # Greek letters
    r"\u2070-\u209F"         # Superscripts/Subscripts
    r"\u2190-\u21FF"         # Arrows
    r"\u2200-\u22FF"         # Math operators & symbols
    r"]*$"
)

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "llms_config.json")
with open(CONFIG_PATH) as f:
    cfg = json.load(f)

llama_llm_obj = BuildLLm(**cfg["llama"],
                         temperature=0)

qwen_awq_32_llm_obj = BuildLLm(**cfg["qwen"],
                               temperature=0,
                               extra_body={"guided_regex": english_only_regex})

gpt_llm_obj = BuildLLm(model_url=None,
                       model_name="gpt-4.1-mini",
                       api_key=cfg["gpt"]["api_key"],
                       temperature=0)

llama_llm = llama_llm_obj.build_llm()
qwen_llm = qwen_awq_32_llm_obj.build_llm()
gpt_llm = gpt_llm_obj.build_llm()
