from abc import ABC, abstractmethod
from typing import final
from pydantic import BaseModel

import aiohttp
from enum import StrEnum

from src.core.schemas import BaseSchemas


class ApiStatusesEnum(StrEnum):
    ERROR = "error"
    ALREADY_EXISTS = "already_exists"
    SUCCESS = "success"




class BaseApiService(ABC):

    def __init__(self, base_url: str, api_url: str) -> None:
        self._base_url = base_url
        self.api_url = api_url
        self.timeout = aiohttp.ClientTimeout(total=10)
        self.headers = {"Content-Type": "application/json"}

    @final
    async def _send(self, payload: BaseModel) -> ApiStatusesEnum:
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
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

    async def send(
            self,
            user_data: BaseSchemas,
            payload_model: BaseModel
    ) -> ApiStatusesEnum:
        return await self._send(
            payload_model.model_validate(
                user_data.to_dict()
            )
        )
