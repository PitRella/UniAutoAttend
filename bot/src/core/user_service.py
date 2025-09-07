from typing import Dict, Optional
import re

from .models import UserData, UserState
from .locales import Language, detect_language_from_locale


class UserService:
    """Service for managing user data and states."""
    
    def __init__(self) -> None:
        self._users: Dict[int, UserData] = {}
    
    def get_or_create_user(self, user_id: int, locale: Optional[str] = None) -> UserData:
        """Get existing user or create new one."""
        if user_id not in self._users:
            language = detect_language_from_locale(locale) if locale else Language.ENGLISH
            self._users[user_id] = UserData(
                user_id=user_id,
                language=language,
                state=UserState.START
            )
        return self._users[user_id]
    
    def update_user_language(self, user_id: int, language: Language) -> None:
        """Update user language."""
        if user_id in self._users:
            self._users[user_id].language = language
    
    def update_user_state(self, user_id: int, state: UserState) -> None:
        """Update user state."""
        if user_id in self._users:
            self._users[user_id].state = state
    
    def set_user_email(self, user_id: int, email: str) -> None:
        """Set user email."""
        if user_id in self._users:
            self._users[user_id].email = email
    
    def set_user_password(self, user_id: int, password: str) -> None:
        """Set user password."""
        if user_id in self._users:
            self._users[user_id].password = password
    
    def get_user(self, user_id: int) -> Optional[UserData]:
        """Get user by ID."""
        return self._users.get(user_id)
    
    def is_valid_email(self, email: str) -> bool:
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def clear_user_data(self, user_id: int) -> None:
        """Clear user data (for privacy)."""
        if user_id in self._users:
            self._users[user_id].email = None
            self._users[user_id].password = None


# Global user service instance
user_service = UserService()
