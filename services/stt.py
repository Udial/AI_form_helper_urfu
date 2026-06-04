import tempfile
import whisper
from fastapi import UploadFile
from config import settings

_model = None

def get_stt_model():
    global _model
    if _model is None:
        # Используем 'base' для скорости. Для качества можно 'small' или 'medium'
        _model = whisper.load_model("base") 
    return _model

async def transcribe_audio(file: UploadFile) -> str:
    model = get_stt_model()
    
    # Сохраняем во временный файл, т.к. whisper требует путь к файлу
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp.flush()
        
        result = model.transcribe(tmp.name, language="ru", task="transcribe")
        
    return result["text"].strip()