import aiohttp
import logging

from src.core.schemas import UserSchema, CreateUserRequestSchema
from src.services.api.base import BaseApiService

logger = logging.getLogger(__name__)


class UserApiService(BaseApiService):
    """Service for sending data to external API."""


    def __init__(self, base_url: str, api_url: str):
        super().__init__(base_url, api_url)

    async def send(self, user_data: UserSchema) -> bool:
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
                if response.status != 201:
                    logger.error(f"API returned status {response.status} for user {payload.telegram_id}")
                    return False
                return True

