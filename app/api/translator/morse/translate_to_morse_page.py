from fastapi import APIRouter
from app.service.translators.morse import ToMorseTranslator

router = APIRouter(prefix="/translator/morse", tags=["Morse Translator"])
translator = ToMorseTranslator()

@router.get("/to_morse-{text}")
def to_morse(text: str):
    return {"translated_text": translator.translate(text)}
