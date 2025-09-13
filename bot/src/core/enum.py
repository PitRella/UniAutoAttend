from enum import StrEnum


class UserState(StrEnum):
    """User conversation states."""
    START = "start"
    LANGUAGE_SELECTION = "language_selection"
    EMAIL_INPUT = "email_input"
    PASSWORD_INPUT = "password_input"
    GROUP_INPUT = "group_input"
    COMPLETED = "completed"
