
from langchain_core.documents import Document
from langchain_qdrant import QdrantVectorStore

from app.utils import nv_embeddings as embeddings, settings


docs = [
    Document(
        page_content="A bunch of scientists bring back dinosaurs and mayhem breaks loose",
        metadata={"year": 1993, "rating": 7.7, "genre": "science fiction"},
    ),
    Document(
        page_content="Leo DiCaprio gets lost in a dream within a dream within a dream within a ...",
        metadata={"year": 2010, "director": "Christopher Nolan", "rating": 8.2},
    ),
    Document(
        page_content="A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea",
        metadata={"year": 2006, "director": "Satoshi Kon", "rating": 8.6},
    ),
    Document(
        page_content="A bunch of normal-sized women are supremely wholesome and some men pine after them",
        metadata={"year": 2019, "director": "Greta Gerwig", "rating": 8.3},
    ),
    Document(
        page_content="Toys come alive and have a blast doing so",
        metadata={"year": 1995, "genre": "animated"},
    ),
    Document(
        page_content="Three men walk into the Zone, three men walk out of the Zone",
        metadata={
            "year": 1979,
            "rating": 9.9,
            "director": "Andrei Tarkovsky",
            "genre": "science fiction",
        },
    ),
]


def ingest_sample_documents(collection_name: str = "documents"):
    """Pipeline to ingest sample documents"""

    qdrant = QdrantVectorStore.from_documents(docs, embedding=embeddings,
                                              url=settings.qdrant_url,
                                              collection_name=collection_name,
                                              prefer_grpc=False
                                              )

    resp = qdrant.collection_name

    return resp
