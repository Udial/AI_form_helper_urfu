from config import settings
from services.ai.base import AIService
from services.ai.gigachat import GigaChatService

def get_ai_service() -> AIService:
    """Возвращает настроенный экземпляр AI-сервиса"""
    if settings.AI_PROVIDER == "gigachat":
        if not settings.GIGACHAT_CREDENTIALS:
            raise ValueError("Не задан GIGACHAT_CREDENTIALS в .env. Нужен Authorization data из кабинета GigaChat.")

        return GigaChatService(
            credentials=settings.GIGACHAT_CREDENTIALS,
            scope=settings.GIGACHAT_SCOPE
        )
    else:
        raise ValueError(f"Неподдерживаемый AI_PROVIDER: {settings.AI_PROVIDER}")