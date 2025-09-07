from .user import UserService
from .api import ApiService
from .user_validator import UserDataValidator
from .tg_validatior import TelegramValidatorService
from src.core.settings import Settings

settings = Settings.load()

user_service = UserService()
api_service = ApiService(settings.api_settings.url)

__all__ = [
    'UserService',
    'ApiService',
    'TelegramValidatorService',
    'UserDataValidator',
    'user_service',
    'api_service'
]
