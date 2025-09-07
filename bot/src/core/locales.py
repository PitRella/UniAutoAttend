from enum import StrEnum
from typing import Dict, Any


class Language(StrEnum):
    """Supported languages."""
    UKRAINIAN = "uk"
    ENGLISH = "en"


class MessageKey(StrEnum):
    """Message keys for translations."""
    WELCOME = "welcome"
    SELECT_LANGUAGE = "select_language"
    LANGUAGE_SELECTED = "language_selected"
    ENTER_EMAIL = "enter_email"
    ENTER_PASSWORD = "enter_password"
    INVALID_EMAIL = "invalid_email"
    DATA_SENT = "data_sent"
    ERROR_OCCURRED = "error_occurred"
    EMAIL_SENT_SUCCESS = "email_sent_success"


# Translation dictionaries
TRANSLATIONS: Dict[Language, Dict[MessageKey, str]] = {
    Language.UKRAINIAN: {
        MessageKey.WELCOME: "👋 Вітаю! Я бот для автоматичного відвідування університетських занять.",
        MessageKey.SELECT_LANGUAGE: "🌐 Будь ласка, оберіть мову:",
        MessageKey.LANGUAGE_SELECTED: "✅ Мову змінено на українську",
        MessageKey.ENTER_EMAIL: "📧 Будь ласка, введіть вашу електронну пошту:",
        MessageKey.ENTER_PASSWORD: "🔐 Тепер введіть пароль від вашої пошти:",
        MessageKey.INVALID_EMAIL: "❌ Неправильний формат електронної пошти. Спробуйте ще раз:",
        MessageKey.DATA_SENT: "📤 Дані відправлено на сервер...",
        MessageKey.ERROR_OCCURRED: "❌ Виникла помилка. Спробуйте пізніше.",
        MessageKey.EMAIL_SENT_SUCCESS: "✅ Дані успішно відправлено на сервер!"
    },
    Language.ENGLISH: {
        MessageKey.WELCOME: "👋 Welcome! I'm a bot for automatic university attendance.",
        MessageKey.SELECT_LANGUAGE: "🌐 Please select your language:",
        MessageKey.LANGUAGE_SELECTED: "✅ Language changed to English",
        MessageKey.ENTER_EMAIL: "📧 Please enter your email address:",
        MessageKey.ENTER_PASSWORD: "🔐 Now enter your email password:",
        MessageKey.INVALID_EMAIL: "❌ Invalid email format. Please try again:",
        MessageKey.DATA_SENT: "📤 Sending data to server...",
        MessageKey.ERROR_OCCURRED: "❌ An error occurred. Please try again later.",
        MessageKey.EMAIL_SENT_SUCCESS: "✅ Data successfully sent to server!"
    }
}


def get_text(language: Language, key: MessageKey) -> str:
    """Get translated text for given language and key."""
    return TRANSLATIONS.get(language, TRANSLATIONS[Language.ENGLISH]).get(key, str(key))


def detect_language_from_locale(locale: str) -> Language:
    """Detect language from user locale."""
    if locale and locale.startswith('uk'):
        return Language.UKRAINIAN
    return Language.ENGLISH
