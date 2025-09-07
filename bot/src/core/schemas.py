import re

from dataclasses import dataclass
from src.core.enum import UserState
from src.core.locales import Language


@dataclass(kw_only=True, slots=True)
class UserSchema:
    """User data model."""
    telegram_id: int
    language: Language = Language.ENGLISH
    state: UserState = UserState.START
    email: str | None = None
    password: str | None = None
