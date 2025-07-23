import httpx
import os
from dotenv import load_dotenv

load_dotenv()

class ChatbotEngine:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={self.api_key}"
        self.chat_history = []

    def generate_response(self, user_message: str) -> str:
        # Add user message to history
        self.chat_history.append({"role": "user", "parts": [{"text": user_message}]})
        # Prepare the payload for Gemini
        payload = {
            "contents": [
                {"parts": [{"text": self._build_prompt()}]}
            ]
        }
        try:
            response = httpx.post(self.api_url, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            # Parse Gemini's response
            candidates = data.get("candidates", [])
            if candidates and "content" in candidates[0]:
                parts = candidates[0]["content"].get("parts", [])
                if parts and "text" in parts[0]:
                    bot_reply = parts[0]["text"].strip()
                    self.chat_history.append({"role": "model", "parts": [{"text": bot_reply}]})
                    return bot_reply
            return "[No response from Gemini API]"
        except Exception as e:
            return f"[Error contacting Gemini API: {e}]"

    def _build_prompt(self) -> str:
        # Build a simple conversation prompt from history
        prompt = ""
        for turn in self.chat_history:
            if turn["role"] == "user":
                prompt += f"User: {turn['parts'][0]['text']}\n"
            elif turn["role"] == "model":
                prompt += f"Bot: {turn['parts'][0]['text']}\n"
        prompt += "Bot:"
        return prompt

    def reset_history(self):
        self.chat_history = [] 