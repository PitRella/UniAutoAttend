from typing import Annotated

from fastapi import APIRouter, Depends

from src.user.schemas import (
    CreateUserRequestSchema,
    UpdateUserUnivInfoRequestSchema
)
from src.user.services import UserService
from src.core.base import get_service

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


@user_router.patch(
    '/',
    summary='Update university fields',
    status_code=200
)
async def update_user(
        service: Annotated[UserService, Depends(get_service(UserService))],
        user_schema: UpdateUserUnivInfoRequestSchema,
) -> None:
    await service.update_user(user_schema)
