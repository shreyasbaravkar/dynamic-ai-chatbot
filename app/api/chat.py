
from uuid import UUID
from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse, ChatMessage
from app.services.chatbot import generate_reply
from app.services.conversation import (
    get_conversation,
    add_message,
    clear_conversation
)

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    conversation_id = request.conversation_id

    history = get_conversation(conversation_id)

    add_message(
        conversation_id,
        ChatMessage(role="user", content=request.message)
    )

    reply = generate_reply(request.message, history)

    add_message(
        conversation_id,
        ChatMessage(role="assistant", content=reply)
    )

    return ChatResponse(
        conversation_id=conversation_id,
        reply=reply
    )


@router.get("/{conversation_id}/history")
def get_chat_history(conversation_id: UUID):
    history = get_conversation(conversation_id)

    return {
        "conversation_id": conversation_id,
        "messages": history
    }


@router.delete("/{conversation_id}")
def delete_chat(conversation_id: UUID):
    deleted = clear_conversation(conversation_id)

    return {
        "conversation_id": conversation_id,
        "deleted": deleted
    }
