import aiohttp
import logging

from src.core.schemas import UserSchema, CreateUserRequestSchema
from src.services.api.base import BaseApiService

from bot.src.services.api.base import ApiStatusesEnum

logger = logging.getLogger(__name__)


class UserApiService(BaseApiService):
    """Service for sending data to external API."""

    def __init__(self, base_url: str, api_url: str):
        super().__init__(base_url, api_url)

    async def send(self, user_data: UserSchema) -> ApiStatusesEnum:
        """Send user data to the API endpoint."""
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            payload = CreateUserRequestSchema.model_validate(
                user_data.to_dict()
            )
            async with session.post(
                    self.api_url,
                    json=payload.model_dump(),
                    headers=self.headers
            ) as response:
                match response.status:
                    case 409:
                        return ApiStatusesEnum.ALREADY_EXISTS
                    case 201:
                        return ApiStatusesEnum.SUCCESS
                return ApiStatusesEnum.ERROR

