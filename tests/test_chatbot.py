
from fastapi.testclient import TestClient

from app.main import app
from app.services.chatbot import generate_reply

client = TestClient(app)


def test_generate_reply():
    reply = generate_reply("Hello chatbot")

    expected = (
        "You said: Hello chatbot. "
        "The chatbot service is working, but AI integration is not enabled yet."
    )

    assert reply == expected


def test_empty_message_is_rejected():
    response = client.post("/chat/", json={"message": ""})

    assert response.status_code == 422
