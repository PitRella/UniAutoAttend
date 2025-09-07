import re
from pydantic import BaseModel, EmailStr
from dataclasses import dataclass, asdict
from src.core.enum import UserState
from src.core.locales import Language


@dataclass(kw_only=True, slots=True)
class UserSchema:
    """User data model."""
    telegram_id: int
    username: str | None = None
    language: Language = Language.ENGLISH
    state: UserState = UserState.START
    university_email: str | None = None
    university_password: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


class CreateUserRequestSchema(BaseModel):
    telegram_id: int
    university_email: EmailStr
    university_password: str
