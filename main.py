import os
from fastapi import FastAPI
from chatbot_engine import ChatbotEngine
from schemas import UserMessage, BotResponse

# Initialize FastAPI app
app = FastAPI(
    title="Chatbot API",
    description="A simple chatbot using FastAPI and Hugging Face's DialoGPT.",
    version="1.0.0",
)

# Initialize the chatbot engine
chatbot = ChatbotEngine()

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the Chatbot API. Go to /docs to see the endpoints."}

@app.post("/chat", response_model=BotResponse)
async def chat(user_message: UserMessage):
    response = chatbot.generate_response(user_message.message)
    return BotResponse(response=response)

@app.post("/reset")
async def reset_chat():
    chatbot.reset_history()
    return {"message": "Chat history has been reset."}
