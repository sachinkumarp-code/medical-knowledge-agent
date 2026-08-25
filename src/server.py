from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.agent import agent # Your LangGraph agent

app = FastAPI()

# --- SECURITY: CORS CONFIGURATION ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://13.53.70.238:3000"], # Whitelists your Next.js frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat_with_agent(request: ChatRequest):
    response = agent.invoke({"messages": [("user", request.question)]})
    return {"answer": response["messages"][-1].content}
