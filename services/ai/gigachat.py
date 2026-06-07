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
        base_context = (
            "Ты помощник, который помогает студентам заполнять университетскую заявку на проект. "
            "Пиши в официально-деловом стиле. "
            "Верни только готовый текст для вставки в поле формы. "
            "Не добавляй пояснений, комментариев, заголовков, списков и вариантов ответа.\n\n"
            f"Идея проекта: {idea}\n"
            f"Действие пользователя: {action}\n\n"
        )

        prompts = {
            "description": (
                base_context +
                "Нужно заполнить поле «Описание проекта». "
                "Сформулируй описание проекта в 2-4 связанных предложениях. "
                "Опиши суть проекта, его назначение и общую идею реализации."
            ),
            "goals": (
                base_context +
                "Нужно заполнить поле «Цели проекта». "
                "Сформулируй цели проекта в 2-3 связанных предложениях. "
                "Отрази основную цель и практическую значимость проекта."
            ),
            "result": (
                base_context +
                "Нужно заполнить поле «Ожидаемый результат». "
                "Сформулируй ожидаемый результат проекта в 1-3 связанных предложениях. "
                "Опиши итоговый продукт, решение или эффект, который будет получен."
            ),
            "criteria": (
                base_context +
                "Нужно заполнить поле «Критерии успешности». "
                "Сформулируй критерии успешности проекта в 2-4 связанных предложениях. "
                "Опиши, по каким признакам, метрикам или результатам можно будет оценить успех проекта."
            ),
        }

        return prompts.get(
            field,
            base_context +
            f"Нужно заполнить поле «{field}». "
            "Сгенерируй подходящий официальный текст для этого поля."
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