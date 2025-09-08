from .user import UserApiService
from src.core.settings import Settings

settings = Settings.load()

api_service = UserApiService(
    settings.api_settings.url,
    settings.api_settings.user_route,
)