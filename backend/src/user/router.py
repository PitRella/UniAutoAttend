from typing import Annotated

from fastapi import APIRouter, Depends

from src.user.schemas import CreateUserRequestSchema
from src.user.service import UserService
from src.core.dependency import get_service

user_router = APIRouter(prefix='/user', tags=['user'])


@user_router.post(
    '/',
    summary='Create a new user',
    description=(
            'Create a new user account.'
    ),
    status_code=201,
)
async def create_user(
        service: Annotated[UserService, Depends(get_service(UserService))],
        user_schema: CreateUserRequestSchema,
) -> None:
    await service.create_user(user_schema)
