# Gemini Chatbot with FastAPI

A modern, modular chatbot web application using FastAPI (Python), Google Gemini API for AI responses, and a clean HTML/CSS/JS frontend.

---

## Features
- Conversational chatbot powered by Google Gemini API
- FastAPI backend with modular code structure
- Simple, modern web UI (HTML/CSS/JS)
- Chat history and reset functionality
- Secure API key management with `.env`

---

## Getting Started

### 1. **Clone the Repository**
```bash

git clone <https://github.com/arshah-lamees/chatbot.git>
cd <chatbot>
```

### 2. **Set Up a Virtual Environment (Recommended)**
A virtual environment keeps your dependencies isolated.
```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
If you don't have a `requirements.txt`, install manually:
```bash
pip install fastapi uvicorn httpx python-dotenv
```

### 4. **Get a Gemini API Key**
- Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and log in with your Google account.
- Create a new API key.
- **Copy your API key** (you won't be able to see it again).

### 5. **Configure Environment Variables**
Create a `.env` file in your project root:
```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```
**Never share or commit your API key!**

### 6. **Run the App**
```bash
uvicorn main:app --reload
#OR
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
- Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the chat UI.
- Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the API documentation.

---

## Usage
- Type your message in the chat UI and press Send.
- The bot will reply using the Gemini API.
- To reset the conversation, use the `/reset` endpoint in the docs or add a reset button to the UI.

---

## Project Structure
```
├── venv                 # Virtual environment 
├── main.py              # FastAPI app, endpoints, static file serving
├── chatbot_engine.py    # Chatbot logic, Gemini API integration
├── schemas.py           # Pydantic models for request/response
├── .env                 # Your Gemini API key (not committed)
├── .gitignore           # Ignores venv/, .env, etc.
├── static/
│   ├── index.html       # Chat UI
│   ├── style.css        # Chat UI styles
│   └── chat.js          # Chat UI logic
```

---

## Customization
- **Frontend:** Edit `static/index.html`, `style.css`, or `chat.js` for UI changes.
- **Backend:** Edit `chatbot_engine.py` to change how prompts are built or responses are handled.
- **API Key:** Always keep your `.env` file secret!

---

## Troubleshooting
- **API Key Errors:** Make sure your `.env` is correct and you restarted the server after editing it.
- **404/500 Errors:** Check that all files are in place and dependencies are installed.
- **Gemini API Limits:** Free tier has usage limits. For heavy use, check Google’s pricing.

---

## License
This project is for educational purposes. See individual model and API providers for their terms of use. 