import os 


class Settings:
    APP_NAME: str ="Dynamic AI Chatbot"
    APP_VERSION: str ="1.0.0"
    ENVIRONMENT : str = os.getenv("ENVIRONMENT","development")


settings = Settings()

