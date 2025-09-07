import re
from enum import StrEnum

from pydantic import BaseModel, Field, EmailStr, SecretStr, field_validator
from src.core.locales import Language
from src.exceptions.models import BadPasswordSchemaException

PASSWORD_PATTERN = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$'
)

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')


class UserState(StrEnum):
    """User conversation states."""
    START = "start"
    LANGUAGE_SELECTION = "language_selection"
    EMAIL_INPUT = "email_input"
    PASSWORD_INPUT = "password_input"
    COMPLETED = "completed"


class UserData(BaseModel):
    """User data model."""
    telegram_id: int = Field(..., ge=1)
    language: Language = Language.ENGLISH
    state: UserState = UserState.START
    email: EmailStr | None = Field(..., pattern=EMAIL_PATTERN)
    password: SecretStr | None = None

    @field_validator('password', mode='before')
    def validate_password(cls, value: str) -> str:
        """Validate the password using regex."""
        if not PASSWORD_PATTERN.match(value):
            raise BadPasswordSchemaException
        return value
