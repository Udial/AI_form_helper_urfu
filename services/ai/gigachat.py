from gigachat import GigaChat
from services.ai.base import AIService
from schemas import AIRequest, AIResponse


class GigaChatService(AIService):
    def __init__(self, client_id: str, client_secret: str, scope: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope

        self.client = GigaChat(
            credentials=f"{client_id}:{client_secret}",
            scope=scope,
            verify_ssl_certs=False
        )

    def _build_prompt(self, field: str, action: str, idea: str) -> str:
        prompts = {
            "title": (
                "Ты помощник по заполнению студенческой проектной заявки. "
                "Сгенерируй только название проекта. "
                "Требования: 5-12 слов, официальный стиль, без кавычек, без пояснений.\n\n"
                f"Идея проекта: {idea}\n"
                f"Действие пользователя: {action}"
            ),
            "description": (
                "Ты помощник по заполнению студенческой проектной заявки. "
                "Сгенерируй только описание проекта. "
                "Требования: 2-4 предложения, ясно, формально, без списков и без лишнего текста.\n\n"
                f"Идея проекта: {idea}\n"
                f"Действие пользователя: {action}"
            ),
            "goals": (
                "Ты помощник по заполнению студенческой проектной заявки. "
                "Сгенерируй только цели проекта. "
                "Требования: 2-3 предложения, акцент на результате и пользе проекта, без маркированного списка.\n\n"
                f"Идея проекта: {idea}\n"
                f"Действие пользователя: {action}"
            ),
        }

        return prompts.get(
            field,
            (
                "Ты помощник по заполнению студенческой проектной заявки. "
                "Сгенерируй текст для указанного поля формы. "
                "Верни только готовый текст без пояснений.\n\n"
                f"Поле: {field}\n"
                f"Идея проекта: {idea}\n"
                f"Действие пользователя: {action}"
            )
        )

    async def process_request(self, request: AIRequest) -> AIResponse:
        try:
            prompt = self._build_prompt(
                field=request.field,
                action=request.action,
                idea=request.idea
            )

            response = self.client.chat(prompt)
            generated = response.choices[0].message.content.strip()

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