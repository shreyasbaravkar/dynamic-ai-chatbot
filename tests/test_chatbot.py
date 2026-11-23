
from app.services.chatbot import generate_reply


def test_generate_reply():
    reply = generate_reply("Hello chatbot")

    assert isinstance(reply, str)
    assert len(reply) > 0


def test_generate_reply_with_empty_history():
    reply = generate_reply(
        "Hello chatbot",
        conversation_history=[]
    )

    assert isinstance(reply, str)
    assert len(reply) > 0
