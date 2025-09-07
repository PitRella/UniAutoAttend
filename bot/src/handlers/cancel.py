from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from src.core.locales import MessageKey, get_text
from src.core.models import UserState, UserData
from src.services import user_service, TelegramValidatorService
from aiogram.types import (
    CallbackQuery,
    Message,
)

cancel_router = Router(name="cancel")


@cancel_router.callback_query(F.data == "cancel")
async def cancel_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """Handle cancel callback."""
    user_id: int = callback.from_user.id
    user: UserData = TelegramValidatorService.validate_user_data(
        user_service.get_user(user_id))
    previous_message: Message = TelegramValidatorService.validate_previous_message(
        callback.message
    )
    user_service.update_user_state(
        user_id,
        UserState.START
    )
    user_service.clear_user_data(
        user_id
    )

    welcome_text: str = get_text(user.language, MessageKey.WELCOME)
    await previous_message.edit_text(
        f"{welcome_text}\n\n{get_text(user.language, MessageKey.SELECT_LANGUAGE)}"
    )
    await callback.answer()
