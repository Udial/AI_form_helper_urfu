from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Form Helper UrFU"
    API_V1_PREFIX: str = "/api/v1"
    
    # Настройки AI
    AI_PROVIDER: str = "gigachat"
    
    # GigaChat Credentials
    GIGACHAT_CLIENT_ID: str = ""
    GIGACHAT_CLIENT_SECRET: str = ""
    GIGACHAT_SCOPE: str = "GIGACHAT_API_PERS"
    
    # Безопасность
    SECRET_KEY: str = "xK9mP2vL8nQ5wR3tY6uI0oA4sD7fG1hJ2kL5zX8cV3bN6mM9qW0eR4tY7uI1oP3"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    
    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://127.0.0.1:5500", "http://localhost:8000"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()