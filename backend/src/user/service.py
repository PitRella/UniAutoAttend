from sqlalchemy.ext.asyncio.session import AsyncSession

from src.core.dao import BaseDAO
from src.core.service import BaseService
from src.user.schemas import CreateUserRequestSchema
from src.user.models import User


class UserService(BaseService):
    def __init__(
            self,
            db_session: AsyncSession,
            user_dao: BaseDAO | None = None,
    ):
        super().__init__(db_session)
        self._dao = user_dao or BaseDAO[
            User,
            CreateUserRequestSchema,
        ](session=db_session, model=User)

    async def create_user(self, user_schema: CreateUserRequestSchema) -> User:
        async with self._session.begin():
            user: User = await self._dao.create(user_schema)
        return user
