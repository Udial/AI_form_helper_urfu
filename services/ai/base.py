from abc import ABC, abstractmethod
from schemas import AIRequest, AIResponse

class AIService(ABC):
    """Базовый интерфейс. Для метода process_request."""
    
    @abstractmethod
    async def process_request(self, request: AIRequest) -> AIResponse:
        """
        Обрабатывает запрос к AI.
        :param request: Содержит idea, field, action, current_text
        :return: AIResponse с сгенерированным текстом
        """
        pass