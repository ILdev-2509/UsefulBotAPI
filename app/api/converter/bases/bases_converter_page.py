from fastapi import APIRouter
from app.service.converters.bases_converter import BasesConverter

router = APIRouter(prefix="/converter/bases", tags=["Bases Converter"])
converter = BasesConverter()

@router.get("/convert-{from_base}-{to_base}-{number}")
def convert_bases(from_base: int, to_base: int, number: str):
    return {"converted_number": converter.convert(number, to_base, from_base)}
