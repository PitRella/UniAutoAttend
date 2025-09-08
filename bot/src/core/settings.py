from functools import cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
COMMON_CONFIG = SettingsConfigDict(
    env_file=BASE_DIR / '.env',
    env_file_encoding='utf-8',
    extra='ignore',
)


class TelegramSettings(BaseSettings):
    """Token-related settings."""
    model_config = SettingsConfigDict(**COMMON_CONFIG, env_prefix='TG_')

    API_TOKEN: str = ''


class ApiSettings(BaseSettings):
    """API-related settings."""
    model_config = SettingsConfigDict(**COMMON_CONFIG, env_prefix='API_')

    BASE_URL: str = 'http://localhost:8000/api/'
    VERSION: str = 'v1'
    USER_ROUTER: str = 'user'
    GROUP_ROUTER: str = 'group'
    TIMEOUT: int = 10

    @property
    def url(self) -> str:
        """Return the API URL."""
        return f'{self.BASE_URL}{self.VERSION}'

    @property
    def user_route(self) -> str:
        return f'{self.BASE_URL}{self.USER_ROUTER}'

    @property
    def group_route(self) -> str:
        return f'{self.BASE_URL}{self.GROUP_ROUTER}'


class Settings(BaseSettings):
    """Base settings class for the application."""

    model_config = SettingsConfigDict(
        **COMMON_CONFIG,
    )

    # Log level
    LOG_LEVEL: str = 'INFO'

    # Nested settings
    telegram_settings: TelegramSettings = Field(
        default_factory=TelegramSettings
    )
    api_settings: ApiSettings = Field(
        default_factory=ApiSettings
    )

    @classmethod
    @cache
    def load(cls) -> 'Settings':
        """Return a new instance of Settings."""
        return cls()
