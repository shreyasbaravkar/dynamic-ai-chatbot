from fastapi import APIRouter

router = APIRouter(
    tags=["Health"]
)


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Dynamic AI Chatbot"
    }

