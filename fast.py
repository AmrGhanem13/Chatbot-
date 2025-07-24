from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from together import Together
from typing import List, Dict
from fastapi import Request

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Initialize Together API client
client = Together()

# Health check route
@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

# Simple dynamic greeting route
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}"}

# Request model for chat route
class Query(BaseModel):
    userid: str
    message: str

# Request model for LLM route
class ChatRequest(BaseModel):
    query: str

# Response model for LLM route
class ChatResponse(BaseModel):
    answer: str

# Basic test route to receive a user message
@app.post("/chat/")
def chat(query: Query):
    return {"message": f"User {query.userid} says: {query.message}"}

# LLM chatbot endpoint
@app.post("/llm/", response_model=ChatResponse)
def l_l_m(query2: ChatRequest):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[
            {
                "role": "user",
                "content": query2.query
            }
        ]
    )
    model_ans = response.choices[0].message.content
    return ChatResponse(answer=model_ans)

@app.post("/llm/full/", response_model=ChatResponse)
def l_l_m_full(payload: Dict, request: Request):
    messages = payload["messages"]

    # 🧠 Keep only the last 15 messages
    if len(messages) > 15:
        messages = messages[-15:]

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=messages
    )
    model_ans = response.choices[0].message.content
    return ChatResponse(answer=model_ans)