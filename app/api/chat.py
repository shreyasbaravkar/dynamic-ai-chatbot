from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse
from app.services.chatbot import generate_reply

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    reply = generate_reply(request.message)

    return ChatResponse(reply=reply)

