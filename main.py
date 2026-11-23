
from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.chat import router as chat_router

app = FastAPI(
    title="Dynamic AI Chatbot",
    description="An advanced GPT-powered chatbot API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Dynamic AI Chatbot API is running!"}


app.include_router(health_router)
app.include_router(chat_router)
