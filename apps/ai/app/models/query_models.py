"""Class models for the query based pipelines"""
from typing import List
from pydantic import BaseModel
from langchain_core.documents import Document


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    query: str
    answer: str


class RAGQueryResponse(BaseModel):
    query: str
    answer: List[Document]
