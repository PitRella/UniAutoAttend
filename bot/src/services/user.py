from typing import Dict, Optional

from src.core.models import UserState, UserSchema
from src.core.locales import Language, detect_language_from_locale


class UserService:
    """Service for managing user data and states."""
    
    def __init__(self) -> None:
        self._users: Dict[int, UserSchema] = {}
    
    def get_or_create_user(self, telegram_id: int, locale: Optional[str] = None) -> UserSchema:
        """Get existing user or create new one."""
        if telegram_id not in self._users:
            language = detect_language_from_locale(locale) if locale else Language.ENGLISH
            self._users[telegram_id] = UserSchema(
                telegram_id=telegram_id,
                language=language,
                state=UserState.START
            )
        return self._users[telegram_id]
    
    def update_user_language(self, telegram_id: int, language: Language) -> None:
        """Update user language."""
        if telegram_id in self._users:
            self._users[telegram_id].language = language
    
    def update_user_state(self, telegram_id: int, state: UserState) -> None:
        """Update user state."""
        if telegram_id in self._users:
            self._users[telegram_id].state = state
    
    def set_user_email(self, telegram_id: int, email: str) -> None:
        """Set user email."""
        if telegram_id in self._users:
            self._users[telegram_id].email = email
    
    def set_user_password(self, telegram_id, password: str) -> None:
        """Set user password."""
        if telegram_id in self._users:
            self._users[telegram_id].password = password
    
    def get_user(self, telegram_id: int) -> Optional[UserSchema]:
        """Get user by ID."""
        return self._users.get(telegram_id)
    

    def clear_user_data(self, telegram_id: int) -> None:
        """Clear user data (for privacy)."""
        if telegram_id in self._users:
            self._users[telegram_id].email = None
            self._users[telegram_id].password = None


