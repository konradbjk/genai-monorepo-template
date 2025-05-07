from langchain_qdrant import QdrantVectorStore
from .nvidia_models import nv_embeddings as embeddings

from .settings import settings

qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="documents",
    url=settings.qdrant_url,
)
