from fastapi import APIRouter
from app.service.converters.roman_converter import FromRomanConverter, ToRomanConverter

router = APIRouter(prefix="/converter/roman", tags=["Roman Converter"])
from_translator = FromRomanConverter()
to_translator = ToRomanConverter()

@router.get("/from_roman-{number}")
def from_roman(number: int):
    return {"converted_text": from_translator.convert(number)}

@router.get("/to_roman-{number}")
def to_roman(number: str):
    return {"converted_text": to_translator.convert(number)}
