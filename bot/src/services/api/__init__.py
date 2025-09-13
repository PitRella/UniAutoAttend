from .user import UserApiService
from .group import GroupApiService
from src.core.settings import Settings

settings = Settings.load()

api_service = UserApiService(
    settings.api_settings.url,
    settings.api_settings.user_route,
)
group_service = GroupApiService(
    settings.api_settings.url,
    settings.api_settings.group_route,
)
