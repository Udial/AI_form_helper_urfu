from fastapi import FastAPI, Depends, UploadFile, File, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from schemas import AIRequest, AIResponse, TranscribeResponse, ApplicationData, DraftResponse
from services.ai.factory import get_ai_service
from services.stt import transcribe_audio
from services.drafts import save_draft, load_draft, clear_draft
from services.auth import create_access_token, get_current_user

app = FastAPI(title=settings.PROJECT_NAME, version="1.0.0")

# Разрешаем запросы с фронта
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# АВТОРИЗАЦИЯ
@app.post(f"{settings.API_V1_PREFIX}/auth/login")
async def login(username: str = Form(...)):
    """Упрощённый логин для демо. В продакшене здесь будет редирект на sso.urfu.ru"""
    token = create_access_token(user_id=username)
    return {"access_token": token, "token_type": "bearer"}

# AI АССИСТЕНТ
@app.post(f"{settings.API_V1_PREFIX}/ai/assist", response_model=AIResponse)
async def ai_assist(request: AIRequest, user_id: str = Depends(get_current_user)):
    """Обработка кнопок: Сгенерировать, Улучшить текст, Перегенерировать"""
    ai_service = get_ai_service()
    return await ai_service.process_request(request)

# АУДИО (STT)
@app.post(f"{settings.API_V1_PREFIX}/ai/transcribe", response_model=TranscribeResponse)
async def transcribe(audio: UploadFile = File(...), user_id: str = Depends(get_current_user)):
    """Приём аудио с микрофона и возврат текста"""
    if not audio.content_type or not audio.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Разрешены только аудиофайлы")
    
    try:
        text = await transcribe_audio(audio)
        return TranscribeResponse(success=True, text=text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка распознавания: {str(e)}")

# ЧЕРНОВИКИ
@app.post(f"{settings.API_V1_PREFIX}/drafts/save", response_model=DraftResponse)
async def save_app_draft(data: ApplicationData, user_id: str = Depends(get_current_user)):
    save_draft(user_id, data)
    return DraftResponse(success=True, data=data, message="Черновик сохранён")

@app.get(f"{settings.API_V1_PREFIX}/drafts/load", response_model=DraftResponse)
async def load_app_draft(user_id: str = Depends(get_current_user)):
    data = load_draft(user_id)
    if data:
        return DraftResponse(success=True, data=data, message="Черновик загружен")
    return DraftResponse(success=False, data=None, message="Черновик не найден")

@app.delete(f"{settings.API_V1_PREFIX}/drafts/clear", response_model=DraftResponse)
async def clear_app_draft(user_id: str = Depends(get_current_user)):
    clear_draft(user_id)
    return DraftResponse(success=True, data=None, message="Черновик сброшен")

# ОТПРАВКА ЗАЯВКИ
@app.post(f"{settings.API_V1_PREFIX}/applications/submit")
async def submit_application(data: ApplicationData, user_id: str = Depends(get_current_user)):
    """
    TODO: Здесь будет интеграция с partner.urfu.ru 
    (Playwright автоматизация или прямой API вызов, если он появится)
    """
    clear_draft(user_id) # Очищаем черновик после успешной отправки
    return {
        "success": True, 
        "message": "Заявка успешно отправлена в систему partner.urfu.ru!",
        "application_id": f"URFU-{user_id}-{data.title[:5].upper()}"
    }

@app.get(f"{settings.API_V1_PREFIX}/health")
async def health_check():
    return {"status": "ok", "ai_provider": settings.AI_PROVIDER}