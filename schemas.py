from pydantic import BaseModel, Field
from typing import Optional, Literal

# --- AI Ассистент ---
class AIRequest(BaseModel):
    idea: str = Field(..., min_length=5, description="Идея проекта от пользователя")
    field: Literal["goal", "result", "criteria", "description"] = Field(
        ..., description="Целевое поле формы"
    )
    action: Literal["generate", "improve", "regenerate"] = Field(
        default="generate", description="Действие"
    )
    current_text: Optional[str] = Field(None, description="Текущий текст поля (для action='improve')")

class AIResponse(BaseModel):
    success: bool
    field: str
    generated_text: str
    message: str

# --- Аудио ---
class TranscribeResponse(BaseModel):
    success: bool
    text: str

# --- Форма заявки ---
class ApplicationData(BaseModel):
    title: str = Field(..., description="Название проекта")
    semester: str = Field(..., description="Семестр реализации")
    goal: str = Field(..., description="Цель")
    result: str = Field(..., description="Результат (продукт)")
    criteria: str = Field(..., description="Критерии приемки")
    description: str = Field(..., description="Описание проекта")

class DraftResponse(BaseModel):
    success: bool
    data: Optional[ApplicationData] = None
    message: str