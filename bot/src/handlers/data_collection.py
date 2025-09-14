from aiogram import Router, F
from aiogram.fsm.context import FSMContext

from src.core.locales import MessageKey, get_text
from src.core.schemas import UserSchema
from src.core.enum import UserState
from src.services.validators import (
    UserDataValidator,
    TelegramValidatorService
)
from src.services import user_service
from src.services.api import api_service, group_service
from aiogram.types import (
    User,
    Message,
)

from src.core.schemas import (
    CreateUserRequestSchema,
    SetGroupForUserRequestSchema
)
from src.services.api.base import ApiStatusesEnum

data_collection_router = Router(name="data_collection")


@data_collection_router.message(F.text)
async def text_message_handler(message: Message, state: FSMContext) -> None:
    """Handle text messages for data collection."""
    user_id: int = TelegramValidatorService.validate_user_id(
        message.from_user
    )
    user_data: UserSchema = TelegramValidatorService.validate_user_data(
        user_service.get_user(user_id)
    )
    text: str = TelegramValidatorService.validate_message(
        message.text
    ).strip()
    match user_data.state:
        case UserState.EMAIL_INPUT:
            await handle_email_input(message, user_data, text)
        case UserState.PASSWORD_INPUT:
            await handle_password_input(message, user_data, text)
        case UserState.GROUP_INPUT:
            await handle_group_input(message, user_data, text)


async def handle_email_input(
        message: Message,
        user_data: UserSchema,
        email: str
) -> None:
    if not UserDataValidator.is_valid_email(email):
        await message.answer(
            get_text(user_data.language, MessageKey.INVALID_EMAIL)
        )
        return
    user_service.set_user_email(
        user_data.telegram_id,
        email
    )
    user_service.update_user_state(
        user_data.telegram_id,
        UserState.PASSWORD_INPUT
    )
    await message.answer(
        get_text(
            user_data.language,
            MessageKey.ENTER_PASSWORD
        )
    )


async def handle_password_input(
        message: Message,
        user_data: UserSchema,
        password: str
) -> None:
    """Handle password input."""
    # Save password
    if not UserDataValidator.is_valid_password(password):
        await message.answer(
            get_text(user_data.language, MessageKey.INVALID_PASSWORD)
        )
        return
    user_service.set_user_password(
        user_data.telegram_id,
        password
    )

    await message.answer(
        get_text(user_data.language, MessageKey.USER_DATA_SENT)
    )
    user: User = TelegramValidatorService.validate_user(message.from_user)
    user_data.username = user.username
    api_status = await api_service.send(
        user_data=user_data,
        payload_model=CreateUserRequestSchema
    )
    match api_status:
        case ApiStatusesEnum.ALREADY_EXISTS:
            await message.answer(
                get_text(
                    user_data.language,
                    MessageKey.USER_ALREADY_EXISTS
                )
            )
            user_service.update_user_state(
                user_data.telegram_id,
                UserState.GROUP_INPUT
            )
            await message.answer(
                get_text(user_data.language, MessageKey.ENTER_GROUP)
            )
        case ApiStatusesEnum.SUCCESS:
            await message.answer(
                get_text(
                    user_data.language,
                    MessageKey.EMAIL_SENT_SUCCESS
                )
            )
            user_service.update_user_state(
                user_data.telegram_id,
                UserState.GROUP_INPUT
            )
            await message.answer(
                get_text(user_data.language, MessageKey.ENTER_GROUP)
            )
        case _:
            await message.answer(
                get_text(user_data.language, MessageKey.ERROR_OCCURRED)
            )


async def handle_group_input(
        message: Message,
        user_data: UserSchema,
        group: str
) -> None:
    if not UserDataValidator.is_valid_group(group):
        await message.answer(
            get_text(user_data.language, MessageKey.INVALID_GROUP)
        )
        return
    user_service.set_user_group(
        user_data.telegram_id,
        group
    )
    await message.answer(
        get_text(user_data.language, MessageKey.USER_DATA_SENT)
    )
    user: User = TelegramValidatorService.validate_user(message.from_user)
    user_data.username = user.username
    api_status = await group_service.send(
        user_data=user_data,
        payload_model=SetGroupForUserRequestSchema
    )
    match api_status:
        case ApiStatusesEnum.SUCCESS:
            await message.answer(
                get_text(
                    user_data.language,
                    MessageKey.GROUP_SENT_SUCCESS
                )
            )
            user_service.update_user_state(
                user_data.telegram_id,
                UserState.GROUP_INPUT
            )
        case _:
            await message.answer(
                get_text(user_data.language, MessageKey.ERROR_OCCURRED)
            )
    user_service.clear_user_data(user_data.telegram_id)
