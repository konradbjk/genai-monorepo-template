import os
from langchain_openai import OpenAIEmbeddings
from .settings import settings


embeddings = OpenAIEmbeddings(
    base_url="https://api.aimlapi.com/v1",
    model="text-embedding-3-large",
    api_key=settings.openai_api_key
)
