import re
from pydantic import BaseModel, EmailStr
from dataclasses import dataclass, asdict
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

    def to_dict(self) -> dict:
        return asdict(self)
