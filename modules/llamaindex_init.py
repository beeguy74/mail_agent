
from typing import Tuple
from llama_index.llms.openrouter import OpenRouter
from os import getenv


def init_models(llm_name) -> Tuple[OpenRouter]:
    """
    Initialize the llm and the embedding models, and return them
    """
    llm = None
    try:
        llm = OpenRouter(llm_name)
    except Exception as e:
        print(f"Error while loading the llm: {e}")


    return llm

