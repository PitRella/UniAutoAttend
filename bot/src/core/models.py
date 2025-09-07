from dataclasses import dataclass
from typing import Optional
from enum import Enum

from .locales import Language


class UserState(Enum):
    """User conversation states."""
    START = "start"
    LANGUAGE_SELECTION = "language_selection"
    EMAIL_INPUT = "email_input"
    PASSWORD_INPUT = "password_input"
    COMPLETED = "completed"


@dataclass
class UserData:
    """User data model."""
    user_id: int
    language: Language = Language.ENGLISH
    state: UserState = UserState.START
    email: Optional[str] = None
    password: Optional[str] = None
    
    def is_data_complete(self) -> bool:
        """Check if all required data is collected."""
        return self.email is not None and self.password is not None
