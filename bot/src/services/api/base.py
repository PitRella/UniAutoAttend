from abc import ABC, abstractmethod

import aiohttp
from enum import StrEnum


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

    @abstractmethod
    def send(self, *args, **kwargs) -> ApiStatusesEnum:
        pass
