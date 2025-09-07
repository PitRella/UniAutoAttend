from .user import UserService
from .api import ApiService
from .validator import TelegramValidatorService
from src.core.settings import Settings

settings = Settings.load()

user_service = UserService()
api_service = ApiService(settings.api_settings.url)

__all__ = [
    'UserService',
    'ApiService',
    'TelegramValidatorService',
    'user_service',
    'api_service'
]
