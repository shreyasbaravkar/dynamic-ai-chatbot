from fastapi import FastAPI

app= FastAPI(
    title="Dynamic AI Chatbot",
    description ="An advanced GPT-powered chatbot API",
    version ="1.0.0"
)

@app.get("/")
def home():
    return{"message": "Dynamic AI Chatbot API is running!"}

@app.get("/health")
def health_check():
    return{"status": "healthy"}

