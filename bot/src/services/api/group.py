import aiohttp
import logging

from src.core.schemas import UserSchema, CreateUserRequestSchema, \
    SetGroupForUserRequestSchema
from src.services.api.base import BaseApiService

from src.services.api.base import ApiStatusesEnum

logger = logging.getLogger(__name__)


class GroupApiService(BaseApiService):
    """Service for sending data to external API."""


    def __init__(self, base_url: str, api_url: str):
        super().__init__(base_url, api_url)

