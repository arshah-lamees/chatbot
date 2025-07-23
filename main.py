import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from chatbot_engine import ChatbotEngine
from schemas import UserMessage, BotResponse
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(
    title="Chatbot API",
    description="A simple chatbot using FastAPI and Gemini API.",
    version="1.0.0",
)

# Serve static files (frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_index():
    return FileResponse(os.path.join("static", "index.html"))

# Initialize the chatbot engine
chatbot = ChatbotEngine()

# --- API Endpoints ---
@app.post("/chat", response_model=BotResponse)
async def chat(user_message: UserMessage):
    response = chatbot.generate_response(user_message.message)
    return BotResponse(response=response)

@app.post("/reset")
async def reset_chat():
    chatbot.reset_history()
    return {"message": "Chat history has been reset."}
