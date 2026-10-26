
def generate_reply(message: str) -> str:
    """
    Generate a temporary reply for the supplied message.

    This placeholder will later be replaced by our GPT-powered
    response generation and RAG pipeline.
    """
    cleaned_message = message.strip()

    return (
        f"You said: {cleaned_message}. "
        "The chatbot service is working, but AI integration is not enabled yet."
    )
