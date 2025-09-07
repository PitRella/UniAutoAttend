from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import User as TgUser

from aiogram.types import InlineKeyboardMarkup
from src.core.locales import Language, MessageKey, get_text
from src.core.keyboards import get_language_keyboard
from src.core.models import UserState, UserData
from src.exceptions import NoUserException
from src.services import user_service

start_router = Router(name="start")


@start_router.message(Command("start"))
async def command_start_handler(
        message: Message,
        state: FSMContext
) -> None:
    user: TgUser | None = message.from_user
    if not user:
        raise NoUserException
    user_id: int = user.id
    locale: str | None = user.language_code

    user_data: UserData = user_service.get_or_create_user(
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
async def language_selection_handler(callback: CallbackQuery,
                                     state: FSMContext) -> None:
    """Handle language selection."""
    user_id = callback.from_user.id
    language_code = callback.data.split("_")[1]

    try:
        language = Language(language_code)
        user = user_service.get_user(user_id)

        if user:
            # Update user language
            user_service.update_user_language(user_id, language)

            # Send confirmation
            confirmation_text = get_text(language,
                                         MessageKey.LANGUAGE_SELECTED)
            await callback.message.edit_text(confirmation_text)

            # Ask for email
            await callback.message.answer(
                get_text(language, MessageKey.ENTER_EMAIL)
            )

            # Update state
            user_service.update_user_state(user_id, UserState.EMAIL_INPUT)

        await callback.answer()

    except ValueError:
        await callback.answer("Invalid language selection", show_alert=True)
