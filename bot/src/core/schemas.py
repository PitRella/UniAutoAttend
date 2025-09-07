import re

from pydantic import BaseModel, Field, EmailStr, SecretStr

from src.core.enum import UserState
from src.core.locales import Language

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')


class UserSchema(BaseModel):
    """User data model."""
    telegram_id: int = Field(..., ge=1)
    language: Language = Language.ENGLISH
    state: UserState = UserState.START
    email: EmailStr | None = Field(None, pattern=EMAIL_PATTERN)
    password: SecretStr | None = None
