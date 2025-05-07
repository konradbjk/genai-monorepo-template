""" Self-query retriever pipelines"""

from typing import List
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever
from app.utils import o4_mini as llm, qdrant as vectorestore

prompt_template = PromptTemplate.from_template(
    "You are a product expert. Answer the question in English:\n\nQuestion: {text}"
)

metadata_field_info = [
    AttributeInfo(
        name="genre",
        description="The genre of the movie",
        type="string or list[string]",
    ),
    AttributeInfo(
        name="year",
        description="The year the movie was released",
        type="integer",
    ),
    AttributeInfo(
        name="director",
        description="The name of the movie director",
        type="string",
    ),
    AttributeInfo(
        name="rating", description="A 1-10 rating for the movie", type="float"
    ),
]

document_content_description = "Brief summary of a movie"


def self_query_documents(query: str) -> List[Document] | []:
    """Pipeline - Self-Query Retriever

    Args:
        query (str): string which is used to create queries

    Returns:
        List[Document]: list of documents found, could be empty
    """

    retriever = SelfQueryRetriever.from_llm(
        llm, vectorestore, document_content_description, metadata_field_info, verbose=True
    )

    resp = retriever.invoke(query)

    return resp
