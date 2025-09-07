import re

from dataclasses import dataclass
from src.core.enum import UserState
from src.core.locales import Language

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

@dataclass(kw_only=True, slots=True)
class UserSchema:
    """User data model."""
    telegram_id: int
    language: Language = Language.ENGLISH
    state: UserState = UserState.START
    email: str | None
    password: str | None
