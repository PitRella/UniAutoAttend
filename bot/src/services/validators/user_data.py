import re

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
GROUP_PATTERN = re.compile(r'^^[A-Za-zА-Яа-яІіЇїЄєҐґ]+-\d{2}-\d$')

class UserDataValidator:
    @classmethod
    def is_valid_email(cls, email: str) -> bool:
        return re.match(EMAIL_PATTERN, email) is not None

    @classmethod
    def is_valid_password(cls, password: str) -> bool:
        return len(password) >= 6 and " " not in password

    @classmethod
    def is_valid_group(cls, group: str) -> bool:
        return re.match(GROUP_PATTERN, group) is not None
