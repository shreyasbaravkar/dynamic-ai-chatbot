
from pydantic import BaseModel, Field
from typing import List, Literal
from uuid import UUID, uuid4


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(..., min_length=1, max_length=4000)


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=4000
    )

    conversation_id: UUID = Field(default_factory=uuid4)

    conversation_history: List[ChatMessage] = Field(
        default_factory=list
    )


class ChatResponse(BaseModel):
    conversation_id: UUID
    reply: str
