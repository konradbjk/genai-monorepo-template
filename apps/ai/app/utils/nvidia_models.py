from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from .settings import settings

nv_embeddings = NVIDIAEmbeddings(model="nvidia/nv-embedqa-e5-v5",
                                 api_key=settings.nvidia_api_key
                                 )
