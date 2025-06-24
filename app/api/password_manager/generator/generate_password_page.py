from fastapi import APIRouter
from app.service.password_manager.password_generator import PasswordGenerator

router = APIRouter(prefix="/password_manager/generator", tags=["Password Generator"])
generator = PasswordGenerator()

@router.get("/generate-{length}")
def generate_password(length: int):
    return {"password": generator.generate(length)}
