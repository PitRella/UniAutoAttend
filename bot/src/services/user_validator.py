import re

from src.core.schemas import EMAIL_PATTERN


class UserDataValidator:
    @classmethod
    def is_valid_email(self, email: str) -> bool:
        return re.match(EMAIL_PATTERN, email) is not None

    @classmethod
    def is_valid_password(self, password: str) -> bool:
        return len(password) >= 6 and " " not in password
