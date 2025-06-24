from fastapi import APIRouter
from app.service.translators.keyboard import KeyboardTranslator

router = APIRouter(prefix="/translator/keyboard", tags=["Keyboard Translator"])

@router.get("/keyboard-{text}-{direction}")
def keyboard(text: str, direction: str):
    translator = KeyboardTranslator(direction=direction)
    return {"translated_text": translator.translate(text)}
