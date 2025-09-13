from enum import StrEnum
from typing import Dict, Any, Union


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
    ENTER_GROUP = "enter_group"
    INVALID_EMAIL = "invalid_email"
    INVALID_PASSWORD = "invalid_password"
    INVALID_GROUP = "invalid_group"
    USER_DATA_SENT = "user_data_sent"
    GROUP_DATA_SENT = "group_data_sent"
    ERROR_OCCURRED = "error_occurred"
    EMAIL_SENT_SUCCESS = "email_sent_success"
    GROUP_SENT_SUCCESS = "group_sent_success"
    CURRENT_SUFFIX = "current_suffix"
    CANCEL = "cancel"


class LanguageLabelKey(StrEnum):
    """Keys for language display names."""
    UK = "uk"
    EN = "en"


# Translation dictionaries
# Allow both message keys and language label keys
TRANSLATIONS: Dict[
    Language, Dict[Union[MessageKey, LanguageLabelKey], str]] = {
    Language.UKRAINIAN: {
        MessageKey.WELCOME: "👋 Вітаю! Я бот для автоматичного відвідування університетських занять.",
        MessageKey.SELECT_LANGUAGE: "🌐 Будь ласка, оберіть мову:",
        MessageKey.LANGUAGE_SELECTED: "✅ Мову змінено на українську",
        MessageKey.ENTER_EMAIL: "📧 Будь ласка, введіть вашу електронну пошту:",
        MessageKey.ENTER_PASSWORD: "🔐 Тепер введіть пароль від вашої пошти:",
        MessageKey.ENTER_GROUP: "👥 Введіть назву вашої групи",
        MessageKey.INVALID_EMAIL: "❌ Неправильний формат електронної пошти. Спробуйте ще раз:",
        MessageKey.INVALID_PASSWORD: "❌ Неправильний формат паролю. Спробуйте ще раз:",
        MessageKey.INVALID_GROUP: "❌ Неправильний формат группи. Спробуйте ще раз:",
        MessageKey.USER_DATA_SENT: "📤 Дані відправлено на сервер...",
        MessageKey.ERROR_OCCURRED: "❌ Виникла помилка. Спробуйте пізніше.",
        MessageKey.EMAIL_SENT_SUCCESS: "✅ Дані успішно відправлено на сервер!",
        MessageKey.GROUP_SENT_SUCCESS: "✅ Дані успішно відправлено на сервер!",
        LanguageLabelKey.UK: "Українська",
        LanguageLabelKey.EN: "Англійська",
        MessageKey.CURRENT_SUFFIX: " (Поточна)",
        MessageKey.CANCEL: "❌ Скасувати",
    },
    Language.ENGLISH: {
        MessageKey.WELCOME: "👋 Welcome! I'm a bot for automatic university attendance.",
        MessageKey.SELECT_LANGUAGE: "🌐 Please select your language:",
        MessageKey.LANGUAGE_SELECTED: "✅ Language changed to English",
        MessageKey.ENTER_EMAIL: "📧 Please enter your email address:",
        MessageKey.ENTER_PASSWORD: "🔐 Now enter your email password:",
        MessageKey.ENTER_GROUP: "👥 Please enter your group name:",
        MessageKey.INVALID_EMAIL: "❌ Invalid email format. Please try again:",
        MessageKey.INVALID_PASSWORD: "❌ Invalid password format. Please try again:",
        MessageKey.INVALID_GROUP: "❌ Invalid group format. Please try again:",
        MessageKey.USER_DATA_SENT: "📤 Sending data to server...",
        MessageKey.ERROR_OCCURRED: "❌ An error occurred. Please try again later.",
        MessageKey.EMAIL_SENT_SUCCESS: "✅ Data successfully sent to server!",
        LanguageLabelKey.UK: "Ukrainian",
        LanguageLabelKey.EN: "English",
        MessageKey.CURRENT_SUFFIX: " (Current)",
        MessageKey.CANCEL: "❌ Cancel",
    }
}


def get_text(
        language: Language,
        key: Union[
            MessageKey,
            LanguageLabelKey
        ]
) -> str:
    """Get translated text for given language and key."""
    return TRANSLATIONS.get(
        language,
        TRANSLATIONS[Language.ENGLISH]
    ).get(
        key,
        str(key)
    )


def detect_language_from_locale(locale: str | None) -> Language:
    match locale:
        case 'uk':
            return Language.UKRAINIAN
        case 'en':
            return Language.ENGLISH
    return Language.ENGLISH
