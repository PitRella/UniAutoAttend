from sqlalchemy.ext.asyncio.session import AsyncSession

from src.core.dao import BaseDAO
from src.core.service import BaseService
from src.user.schemas import (
    CreateGroupRequestSchema,
)
from src.user.models import Group, User


class GroupService(BaseService):
    def __init__(
            self,
            db_session: AsyncSession,
            group_dao: BaseDAO | None = None,
            user_dao: BaseDAO | None = None,
    ):
        super().__init__(db_session)
        self._dao = group_dao or BaseDAO[
            Group,
            CreateGroupRequestSchema,
        ](session=db_session, model=Group)
        self._user_dao = user_dao or BaseDAO[
            User,
        ](session=db_session, model=User)

    async def attach_group_to_user(
            self,
            group_schema: CreateGroupRequestSchema
    ) -> None:
        group_data = group_schema.model_dump()
        telegram_id = group_data.pop('telegram_id')
        async with self._session.begin():
            group: Group | None = await self._dao.get_one(
                name=group_data['name']
            )
            if not group:
                group: Group = await self._dao.create(group_data)
            await self._user_dao.update(
                {
                    "group_id": group.id
                },
                telegram_id=telegram_id
            )
        return None
