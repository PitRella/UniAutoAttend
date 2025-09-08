from .user import UserService
from .api import ApiService
from src.core.settings import Settings

settings = Settings.load()

user_service = UserService()
api_service = ApiService(
    settings.api_settings.url,
    settings.api_settings.user_route,
    settings.api_settings.group_route
)

__all__ = [
    'UserService',
    'ApiService',
    'user_service',
    'api_service'
]
