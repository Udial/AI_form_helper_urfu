from services.ai.base import AIService
from schemas import AIRequest, AIResponse

class GigaChatService(AIService):
    def __init__(self, client_id: str, client_secret: str, scope: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        # TODO: Инициализация клиента GigaChat SDK или requests session

    async def process_request(self, request: AIRequest) -> AIResponse:
        try:
            # =================================================================
            # 1. Сформировать промт на основе request.field, request.action, request.idea
            # 2. Вызвать API GigaChat
            # 3. Распарсить ответ
            # =================================================================
            
            # ВРЕМЕННАЯ ЗАГЛУШКА
            generated = f"[GigaChat сгенерировал текст для поля '{request.field}' на основе идеи: {request.idea[:30]}...]"
            
            return AIResponse(
                success=True,
                field=request.field,
                generated_text=generated,
                message="Текст успешно сгенерирован"
            )
            
        except Exception as e:
            return AIResponse(
                success=False,
                field=request.field,
                generated_text="",
                message=f"Ошибка AI-сервиса: {str(e)}"
            )