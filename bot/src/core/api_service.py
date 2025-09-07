import aiohttp
import asyncio
import logging

from src.core.settings import Settings
settings = Settings.load()
from .models import UserData

logger = logging.getLogger(__name__)


class ApiService:
    """Service for sending data to external API."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.timeout = aiohttp.ClientTimeout(total=10)
    
    async def send_user_data(self, user_data: UserData) -> bool:
        """Send user data to the API endpoint."""
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.post(
                    f"{self.base_url}/user",
                    json=user_data.to_dict(),
                    headers={"Content-Type": "application/json"}
                ) as response:
                    if response.status == 200:
                        logger.info(f"Successfully sent data for user {user_data.user_id}")
                        return True
                    else:
                        logger.error(f"API returned status {response.status} for user {user_data.user_id}")
                        return False
                        
        except asyncio.TimeoutError:
            logger.error(f"Timeout when sending data for user {user_data.user_id}")
            return False
        except Exception as e:
            logger.error(f"Error sending data for user {user_data.user_id}: {e}")
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


api_service = ApiService(settings.api_settings.url)
