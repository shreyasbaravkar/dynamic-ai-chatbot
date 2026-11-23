
import ollama


def generate_reply(message: str, conversation_history=None) -> str:
    """
    Generate a response using the local Llama 3.2 model.
    """

    messages = []

    # Include previous conversation context
    if conversation_history:
        for item in conversation_history:
            messages.append({
                "role": item.role,
                "content": item.content
            })

    # Add the latest user message
    messages.append({
        "role": "user",
        "content": message
    })

    try:
        response = ollama.chat(
            model="llama3.2",
            messages=messages
        )

        return response["message"]["content"]

    except Exception as error:
        return f"Local AI service error: {str(error)}"
