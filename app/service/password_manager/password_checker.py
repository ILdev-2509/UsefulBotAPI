from typing import List, TypedDict
from app.base.api_base import BasePasswordRuleStrategy
from app.base.api_base import BaseChecker

class PasswordCheckResult(TypedDict):
    score: int
    problems: List[str]

class PasswordChecker(BaseChecker):
    def __init__(self, rules: List[BasePasswordRuleStrategy]):
        if not isinstance(rules, list) or not all(isinstance(r, BasePasswordRuleStrategy) for r in rules):
            raise ValueError("rules должен быть списком BasePasswordRuleStrategy")
        self._rules = rules

    def check(self, password: str) -> PasswordCheckResult:
        """
        проверяет пароль согласно переданным правилам
        Args:
            password: пароль для проверки
        Returns:
            PasswordCheckResult: итоговый счет от 0 до 5 и список проблем
        """
        if not isinstance(password, str):
            return {"score": 0, "problems": ["Пароль должен быть строкой"]}

        score = 0
        problems: list[str] = []
        for rule in self._rules:
            ok, msg = rule.validate(password)
            if ok:
                score += 1
            else:
                problems.append(msg)
        return {"score": score, "problems": problems}
