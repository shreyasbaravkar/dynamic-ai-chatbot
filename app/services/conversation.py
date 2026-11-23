
from uuid import UUID

from sqlalchemy import select

from app.core.database import SessionLocal
from app.models.chat import ChatMessage
from app.models.database import Conversation, Message


def get_conversation(conversation_id: UUID) -> list[ChatMessage]:
    """Retrieve messages from PostgreSQL."""
    with SessionLocal() as db:
        messages = db.scalars(
            select(Message)
            .where(Message.conversation_id == conversation_id)
            .order_by(Message.id)
        ).all()

        return [
            ChatMessage(role=msg.role, content=msg.content)
            for msg in messages
        ]


def add_message(conversation_id: UUID, message: ChatMessage) -> None:
    """Save a message permanently in PostgreSQL."""
    with SessionLocal.begin() as db:
        conversation = db.get(Conversation, conversation_id)

        if conversation is None:
            conversation = Conversation(id=conversation_id)
            db.add(conversation)

        db.add(
            Message(
                conversation_id=conversation_id,
                role=message.role,
                content=message.content,
            )
        )


def clear_conversation(conversation_id: UUID) -> bool:
    """Delete a conversation and its messages."""
    with SessionLocal.begin() as db:
        conversation = db.get(Conversation, conversation_id)

        if conversation is None:
            return False

        db.delete(conversation)
        return True
