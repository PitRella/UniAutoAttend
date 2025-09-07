from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    User,
    CallbackQuery,
    Message,
)

from aiogram.types import InlineKeyboardMarkup
from src.core.locales import Language, MessageKey, get_text
from src.core.keyboards import get_language_keyboard
from src.core.models import UserState, UserSchema
from src.services import user_service, TelegramValidatorService

start_router = Router(name="start")


@start_router.message(Command("start"))
async def command_start_handler(
        message: Message,
        state: FSMContext
) -> None:
    user: User = TelegramValidatorService.validate_user(message.from_user)
    user_id: int = user.id
    locale: str | None = user.language_code
    user_data: UserSchema = user_service.get_or_create_user(
        user_id,
        locale
    )

    welcome_text: str = get_text(
        language=user_data.language,
        key=MessageKey.WELCOME
    )
    keyboard: InlineKeyboardMarkup = get_language_keyboard(
        user_language=user_data.language
    )

    await message.answer(
        f"{welcome_text}\n\n{get_text(user_data.language, MessageKey.SELECT_LANGUAGE)}",
        reply_markup=keyboard
    )

    user_service.update_user_state(user_id, UserState.LANGUAGE_SELECTION)


@start_router.callback_query(F.data.startswith("lang_"))
async def language_selection_handler(
        callback: CallbackQuery,
        state: FSMContext
) -> None:
    """Handle language selection."""
    user_id: int = callback.from_user.id
    callback_data: str = TelegramValidatorService.validate_callback_data(
        callback.data
    )
    previous_message: Message = TelegramValidatorService.validate_previous_message(
        callback.message
    )
    language_code: str = callback_data.split("_")[1]
    try:
        language: Language = Language(language_code)
        user_service.update_user_language(
            user_id,
            language
        )
        confirmation_text: str = get_text(
            language,
            MessageKey.LANGUAGE_SELECTED
        )
        await previous_message.edit_text(
            confirmation_text
        )
        await previous_message.answer(
            get_text(
                language,
                MessageKey.ENTER_EMAIL
            )
        )
        user_service.update_user_state(
            user_id,
            UserState.EMAIL_INPUT
        )
        await callback.answer()

    except ValueError:  # TODO: Raise custom exception
        await callback.answer("Invalid language selection", show_alert=True)
