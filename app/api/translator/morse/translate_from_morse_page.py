from fastapi import APIRouter
from app.service.translators.morse import FromMorseTranslator

router = APIRouter(prefix="/translator/morse", tags=["Morse Translator"])
translator = FromMorseTranslator()

@router.get("/from_morse-{text}")
def from_morse(text: str):
    return {"translated_text": translator.translate(text)}
