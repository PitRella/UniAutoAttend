from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from .locales import Language, MessageKey, LanguageLabelKey, get_text


def get_language_keyboard(user_language: Language) -> InlineKeyboardMarkup:
    """Create language selection keyboard."""
    builder = InlineKeyboardBuilder()
    
    uk_text = get_text(user_language, LanguageLabelKey.UK)
    if user_language == Language.UKRAINIAN:
        uk_text += get_text(user_language, MessageKey.CURRENT_SUFFIX)
    builder.button(text=uk_text, callback_data=f"lang_{Language.UKRAINIAN}")

    en_text = get_text(user_language, LanguageLabelKey.EN)
    if user_language == Language.ENGLISH:
        en_text += get_text(user_language, MessageKey.CURRENT_SUFFIX)
    builder.button(text=en_text, callback_data=f"lang_{Language.ENGLISH}")

    builder.adjust(1)
    return builder.as_markup()


def get_cancel_keyboard(user_language: Language) -> InlineKeyboardMarkup:
    """Create cancel keyboard."""
    builder = InlineKeyboardBuilder()
    cancel_text = get_text(user_language, MessageKey.CANCEL)
    builder.button(text=cancel_text, callback_data="cancel")
    return builder.as_markup()
