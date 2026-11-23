
# Dynamic AI Chatbot (GPT-Powered)

## Project Overview

Dynamic AI Chatbot is a B.Tech Computer Science and
Engineering project that provides an intelligent,
context-aware conversational AI system using a locally
running large language model.

The application generates AI responses and stores
conversation history permanently in PostgreSQL.

## Implemented Features

- AI-powered conversational chatbot
- Local AI inference using Llama 3.2
- Context-aware conversation
- Permanent conversation storage
- Conversation history and deletion APIs
- Responsive dark-themed web interface
- New Chat functionality
- REST API with Swagger documentation
- Basic error handling
- Automated testing using Pytest

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python 3.14
- FastAPI
- Uvicorn
- Pydantic

### Artificial Intelligence
- Ollama
- Llama 3.2

### Database
- PostgreSQL
- SQLAlchemy
- Psycopg
- Alembic

### Development Tools
- Visual Studio Code
- Git
- GitHub
- Pytest

## System Architecture

User Interface
    |
FastAPI Backend
    |
    |-- Ollama + Llama 3.2
    |
    |-- PostgreSQL Database

## Running the Application

Activate the Python virtual environment:

    .\.venv\Scripts\Activate.ps1

Install dependencies:

    python -m pip install -r requirements.txt

Ensure PostgreSQL is running and configure the
database credentials in a local .env file.

Download the AI model:

    ollama pull llama3.2

Ensure the Ollama service is running.

Apply database migrations:

    python -m alembic upgrade head

Start the application:

    python -m uvicorn app.main:app --reload

## Application URLs

- Chatbot: http://127.0.0.1:8000/ui/
- Swagger API: http://127.0.0.1:8000/docs
- Health Check: http://127.0.0.1:8000/health

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Application status |
| GET | /health | Health check |
| POST | /chat/ | Generate AI response |
| GET | /chat/{conversation_id}/history | Retrieve messages |
| DELETE | /chat/{conversation_id} | Delete conversation |

## Testing

Run automated tests:

    python -m pytest tests -v

Current automated test results: 2 tests passed.

## Future Enhancements

- User registration and authentication
- Multi-user support and private conversations
- Sidebar conversation history
- PDF, DOCX and TXT document uploads
- Retrieval-Augmented Generation (RAG)
- Document embeddings and vector search
- Analytics dashboard
- Advanced logging and testing
- Cloud deployment

## Project Status

Currently under active development.

The core chatbot, frontend, backend and PostgreSQL
integration are implemented and tested.

The current version is intended for local demonstration.
Authentication and production security are planned
for future development.

## Developer

Shreyas Baravkar

B.Tech - Computer Science and Engineering
