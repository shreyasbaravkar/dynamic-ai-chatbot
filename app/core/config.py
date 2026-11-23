import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str ="Dynamic AI Chatbot"
    APP_VERSION: str ="1.0.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")


settings = Settings()
