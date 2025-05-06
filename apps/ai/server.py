"""FastAPI Server files"""

from fastapi import FastAPI
from app.routers import pipelines
from dotenv import load_dotenv

load_dotenv("./.env.local")

app = FastAPI()

app.include_router(pipelines)
