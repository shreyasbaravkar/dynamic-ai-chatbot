from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="Dynamic AI Chatbot",
    descriptions="An advanced GPT-powered chatbot API",
    versions="1.0.0",
)

@app.get("/")
def home():
    return {"message": "Dynamic AI Chatbot API is running!"}

app.include_router(health_router)
