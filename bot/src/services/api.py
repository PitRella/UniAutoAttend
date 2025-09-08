import aiohttp
import asyncio
import logging

from src.core.schemas import UserSchema, CreateUserRequestSchema

logger = logging.getLogger(__name__)


class ApiService:
    """Service for sending data to external API."""
    
    def __init__(self, base_url: str, user_router: str, group_route: str):
        self.base_url = base_url
        self.user_route = user_router
        self.group_route = group_route
        self.timeout = aiohttp.ClientTimeout(total=10)
        self.headers = {"Content-Type": "application/json"}
    
    async def send_user_data(self, user_data: UserSchema) -> bool:
        """Send user data to the API endpoint."""
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            payload = CreateUserRequestSchema.model_validate(
                user_data.to_dict()
            )
            async with session.post(
                self.user_route,
                json=payload.model_dump(),
                headers=self.headers
            ) as response:
                if response.status == 201:
                    logger.info(f"Successfully sent data for user {payload.telegram_id}")
                    return True
                else:
                    logger.error(f"API returned status {response.status} for user {payload.telegram_id}")
        return False
                        

    
    async def health_check(self) -> bool:
        """Check if the API is available."""
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f"{self.base_url}/health") as response:
                    return response.status == 200
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return False


