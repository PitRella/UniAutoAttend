from typing import Annotated

from fastapi import APIRouter, Depends

from src.user.schemas import (
     CreateGroupRequestSchema
)
from src.user.services import GroupService
from src.core.base import get_service

group_router = APIRouter(prefix='/group', tags=['group'])

@group_router.post(
    '/',
    summary='Attach user to group',
    status_code=201,
)
async def attach_group_to_user(
        service: Annotated[GroupService, Depends(get_service(GroupService))],
        group_schema: CreateGroupRequestSchema,
) -> None:
    await service.attach_group_to_user(group_schema)