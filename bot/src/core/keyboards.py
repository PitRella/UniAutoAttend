from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from .locales import Language, MessageKey, get_text


def get_language_keyboard(user_language: Language) -> InlineKeyboardMarkup:
    """Create language selection keyboard."""
    builder = InlineKeyboardBuilder()
    
    # Ukrainian button
    uk_text = "🇺🇦 Українська"
    if user_language == Language.UKRAINIAN:
        uk_text += " ✅"
    builder.button(text=uk_text, callback_data=f"lang_{Language.UKRAINIAN}")
    
    # English button
    en_text = "🇺🇸 English"
    if user_language == Language.ENGLISH:
        en_text += " ✅"
    builder.button(text=en_text, callback_data=f"lang_{Language.ENGLISH}")
    
    builder.adjust(1)
    return builder.as_markup()


def get_cancel_keyboard(user_language: Language) -> InlineKeyboardMarkup:
    """Create cancel keyboard."""
    builder = InlineKeyboardBuilder()
    cancel_text = "❌ Скасувати" if user_language == Language.UKRAINIAN else "❌ Cancel"
    builder.button(text=cancel_text, callback_data="cancel")
    return builder.as_markup()
