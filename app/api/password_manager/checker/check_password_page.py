import string
from fastapi import APIRouter
from app.service.password_manager.password_checker import PasswordChecker
from app.service.password_manager.rules import (
    MinLengthRule,
    DigitRule,
    LowercaseRule,
    UppercaseRule,
    SpecialCharRule,
)

router = APIRouter(prefix="/password_manager/checker", tags=["Password Checker"])

@router.get("/check-{password}")
def check_password(password: str):
    checker = PasswordChecker(
        rules=[
            MinLengthRule(min_length=8),
            DigitRule(),
            LowercaseRule(),
            UppercaseRule(),
            SpecialCharRule(special_chars=string.punctuation),
        ]
    )
    return checker.check(password)
