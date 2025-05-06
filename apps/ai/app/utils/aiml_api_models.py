from langchain_openai import ChatOpenAI

from .settings import settings

o4_mini = ChatOpenAI(base_url="https://api.aimlapi.com/v1",
                     model='openai/o4-mini-2025-04-16',
                     api_key=settings.openai_api_key,
                     max_completion_tokens=100000,
                     reasoning_effort="medium"
                     )

tool = {"type": "web_search_preview"}

gpt_41 = ChatOpenAI(base_url="https://api.aimlapi.com/v1",
                    model='openai/gpt-4.1-2025-04-14',
                    api_key=settings.openai_api_key,
                    max_completion_tokens=100000
                    )

# gpt_41 = _gpt_41.bind_tools([tool])
