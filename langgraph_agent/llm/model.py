from langchain_openai import ChatOpenAI
from langgraph_agent.config.settings import API_KEY, MODEL_NAME, BASE_URL

llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=0,
    api_key=API_KEY,
    base_url=BASE_URL
)