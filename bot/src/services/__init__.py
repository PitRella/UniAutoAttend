from .user import UserService
from src.core.settings import Settings

settings = Settings.load()

user_service = UserService()


__all__ = [
    'UserService',
    'user_service',
]
