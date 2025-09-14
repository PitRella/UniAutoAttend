from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.core.base import BaseDAO
from src.core.base import BaseService
from src.user.exceptions import UserAlreadyExistsException
from src.user.schemas import (
    CreateUserRequestSchema,
    UpdateUserUnivInfoRequestSchema
)
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

    async def create_user(self, user_schema: CreateUserRequestSchema) -> None:
        # TODO: Implement user password encryption
        try:
            async with self._session.begin():
                await self._dao.create(user_schema)
        except IntegrityError:
            raise UserAlreadyExistsException
        return None

    async def update_user(
            self,
            user_schema: UpdateUserUnivInfoRequestSchema
    ) -> None:
        user_data = self._validate_schema_for_update_request(user_schema)
        async with self._session.begin():
            await self._dao.update(user_data)
        return None
