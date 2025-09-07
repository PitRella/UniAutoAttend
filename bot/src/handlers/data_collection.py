from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.core.locales import MessageKey, get_text
from src.core.schemas import UserSchema
from src.core.enum import UserState
from src.services import user_service, TelegramValidatorService, \
    UserDataValidator
from src.services import api_service

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

    # Send data to API
    await message.answer(
        get_text(user_data.language, MessageKey.DATA_SENT)
    )

    try:
        username = message.from_user.username or message.from_user.first_name or ""
        user_data.username = username
        success = await api_service.send_user_data(user_data)
        if success:
            await message.answer(
                get_text(
                    user_data.language,
                    MessageKey.EMAIL_SENT_SUCCESS
                )
            )
            user_service.update_user_state(
                user_data.telegram_id,
                UserState.COMPLETED
            )
        else:
            await message.answer(
                get_text(user_data.language, MessageKey.ERROR_OCCURRED)
            )

    except Exception as e:
        await message.answer(
            get_text(user_data.language, MessageKey.ERROR_OCCURRED)
        )

    user_service.clear_user_data(user_data.telegram_id)
