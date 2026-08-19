from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import agent

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat_with_agent(request: ChatRequest):
    response = agent.invoke({"messages": [("user", request.question)]})
    return {"answer": response["messages"][-1].content}
