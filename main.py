from fastapi import FastAPI
import uvicorn

from app.config.loader import config
from app.api.translator.keyboard.translate_keyboard_page import router as keyboard_router
from app.api.translator.morse.translate_from_morse_page import router as from_morse_router
from app.api.translator.morse.translate_to_morse_page import router as to_morse_router
from app.api.converter.roman.roman_converter_page import router as roman_router
from app.api.converter.bases.bases_converter_page import router as bases_router
from app.api.password_manager.checker.check_password_page import router as password_checker_router
from app.api.password_manager.generator.generate_password_page import router as password_generator_router

def main() -> None:
    app = FastAPI(title=config.app_name)
    app.include_router(keyboard_router)
    app.include_router(from_morse_router)
    app.include_router(to_morse_router)
    app.include_router(roman_router)
    app.include_router(bases_router)
    app.include_router(password_checker_router)
    app.include_router(password_generator_router)
    uvicorn.run(app)

if __name__ == "__main__":
    main()
