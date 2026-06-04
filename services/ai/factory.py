from config import settings
from services.ai.base import AIService
from services.ai.gigachat import GigaChatService

def get_ai_service() -> AIService:
    """Возвращает настроенный экземпляр AI-сервиса"""
    if settings.AI_PROVIDER == "gigachat":
        return GigaChatService(
            client_id=settings.GIGACHAT_CLIENT_ID,
            client_secret=settings.GIGACHAT_CLIENT_SECRET,
            scope=settings.GIGACHAT_SCOPE
        )
    else:
        raise ValueError(f"Неподдерживаемый AI_PROVIDER: {settings.AI_PROVIDER}")