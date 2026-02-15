from langchain_openai import OpenAIEmbeddings
from functools import lru_cache
from app.config import OPENAI_API_KEY

@lru_cache()
def get_embedding_model():
    return OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=OPENAI_API_KEY
    )