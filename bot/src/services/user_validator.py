import re

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

class UserDataValidator:
    @classmethod
    def is_valid_email(self, email: str) -> bool:
        return re.match(EMAIL_PATTERN, email) is not None

    @classmethod
    def is_valid_password(self, password: str) -> bool:
        return len(password) >= 6 and " " not in password
