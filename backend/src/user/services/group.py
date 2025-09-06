from sqlalchemy.ext.asyncio.session import AsyncSession

from src.core.dao import BaseDAO
from src.core.service import BaseService
from src.user.schemas import (
    CreateGroupRequestSchema,
)
from src.user.models import Group


class GroupService(BaseService):
    def __init__(
            self,
            db_session: AsyncSession,
            group_dao: BaseDAO | None = None,
    ):
        super().__init__(db_session)
        self._dao = group_dao or BaseDAO[
            Group,
            CreateGroupRequestSchema,
        ](session=db_session, model=Group)

    async def attach_group_to_user(
            self,
            group_schema: CreateGroupRequestSchema
    ) -> None:
        group_data = group_schema.model_dump()
        telegram_id = group_data.pop('telegram_id')
        async with self._session.begin():
            group: Group | None = await self._dao.get_one(name=group_data['name'])
            if not group:
                group: Group = await self._dao.create(group_data)
        return None
