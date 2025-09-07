from src.core.models import UserData
from src.exceptions import (
    NoCallbackDataException,
    NoPreviousMessageException,
    NoUserException, NoUserDataExceptions, NoMessageException
)
from aiogram.types import (
    User,
    InaccessibleMessage,
    MaybeInaccessibleMessageUnion,
    Message
)


class TelegramValidatorService:
    @classmethod
    def validate_user_data(cls, user_data: UserData | None) -> UserData:
        if not user_data:
            raise NoUserDataExceptions
        return user_data

    @classmethod
    def validate_user(cls, user: User | None) -> User:
        if not user:
            raise NoUserException
        return user

    @classmethod
    def validate_user_id(cls, user: User | None) -> int:
        validated_user: User = cls.validate_user(user)
        return validated_user.id

    @classmethod
    def validate_callback_data(cls, callback_data: str | None) -> str:
        if not callback_data:
            raise NoCallbackDataException
        return callback_data

    @classmethod
    def validate_previous_message(cls,
                                  previous_message: MaybeInaccessibleMessageUnion | None) -> Message:
        if not previous_message or isinstance(
                previous_message,
                InaccessibleMessage
        ):
            raise NoPreviousMessageException
        return previous_message

    @classmethod
    def validate_message(cls, message: str | None) -> str:
        if not message:
            raise NoMessageException
        return message
