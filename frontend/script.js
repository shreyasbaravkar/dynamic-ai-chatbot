
const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const chatMessages = document.getElementById("chat-messages");
const sendButton = document.getElementById("send-btn");
const newChatButton = document.getElementById("new-chat-btn");

const API_URL = "http://127.0.0.1:8000/chat/";

let conversationId = null;
let isSending = false;

// Display a message safely
function addMessage(role, content) {
    const message = document.createElement("div");

    message.classList.add("message");

    if (role === "user") {
        message.classList.add("user-message");
    } else {
        message.classList.add("bot-message");
    }

    message.textContent = content;
    chatMessages.appendChild(message);

    chatMessages.scrollTop = chatMessages.scrollHeight;

    return message;
}

// Send a message to FastAPI
async function sendMessage(event) {
    event.preventDefault();

    if (isSending) return;

    const message = messageInput.value.trim();

    if (!message) return;

    isSending = true;
    sendButton.disabled = true;

    // Remove welcome screen
    const welcome = document.querySelector(".welcome-screen");
    if (welcome) {
        welcome.remove();
    }

    addMessage("user", message);

    messageInput.value = "";

    const loadingMessage = addMessage(
        "assistant",
        "Thinking..."
    );

    try {
        const requestBody = {
            message: message
        };

        if (conversationId) {
            requestBody.conversation_id = conversationId;
        }

        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody)
        });

        if (!response.ok) {
            throw new Error(
                `Server error: ${response.status}`
            );
        }

        const data = await response.json();

        conversationId = data.conversation_id;

        loadingMessage.textContent = data.reply;

    } catch (error) {
        console.error("Chat error:", error);

        loadingMessage.textContent =
            "Unable to connect to the AI server. Please try again.";
    } finally {
        isSending = false;
        sendButton.disabled = false;
        messageInput.focus();
    }
}

// New conversation
function startNewChat() {
    if (isSending) return;

    conversationId = null;

    chatMessages.innerHTML = `
        <div class="welcome-screen">
            <h1>Welcome to Dynamic AI</h1>
            <p>
                Your intelligent assistant powered by
                Llama 3.2 and FastAPI.
            </p>
            <p>How can I help you today?</p>
        </div>
    `;

    messageInput.value = "";
    messageInput.focus();
}

// Send with Enter; Shift + Enter adds a new line
messageInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();

        if (!isSending) {
            chatForm.requestSubmit();
        }
    }
});

chatForm.addEventListener("submit", sendMessage);
newChatButton.addEventListener("click", startNewChat);
