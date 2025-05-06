
"""Sample router for pipelines"""
from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.models import RAGQueryResponse, QueryResponse
from app.pipelines import ingest_sample_documents

router = APIRouter(prefix="/pipelines", tags=["tasks"])


@router.post("/ingest", response_model=QueryResponse)
def ingest():
    """Endpoint to Ingest documents"""

    try:
        # invoke the pipeline with the user query
        resp = ingest_sample_documents()
        return RAGQueryResponse(query="Sample Ingest", answer="Ingested")
    except Exception as e:
        # handle errors gracefully
        raise HTTPException(
            status_code=500, detail=f"Pipeline error: {e}") from e
