from dataclasses import dataclass
from typing import Optional
from enum import StrEnum

from .dto import BaseDTO
from .locales import Language


class UserState(StrEnum):
    """User conversation states."""
    START = "start"
    LANGUAGE_SELECTION = "language_selection"
    EMAIL_INPUT = "email_input"
    PASSWORD_INPUT = "password_input"
    COMPLETED = "completed"


@dataclass(slots=True)
class UserData(BaseDTO):
    """User data model."""
    user_id: int
    language: Language = Language.ENGLISH
    state: UserState = UserState.START
    email: Optional[str] = None
    password: Optional[str] = None


