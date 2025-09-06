from pydantic import Field, EmailStr
from src.core.schemas import BaseSchema


class CreateUserRequestSchema(BaseSchema):
    telegram_id: int = Field(
        ...,
        ge=0,
        description="Telegram ID"
    )
    username: str = Field(
        ...,
        min_length=5,
        max_length=32,
        description="Telegram username"
    )
    university_email: EmailStr = Field(
        ...,
        min_length=5,
        max_length=255,
        description="University email"
    )
    university_password: str = Field(
        ...,
        min_length=5,
        max_length=255,
        description="University password"
    )


class UpdateUserUnivInfoRequestSchema(BaseSchema):
    telegram_id: int = Field(
        ...,
        ge=0,
        description="Telegram ID"
    )
    university_email: EmailStr | None = Field(
        None,
        min_length=5,
        max_length=255,
        description="University email"
    )
    university_password: str | None = Field(
        None,
        min_length=5,
        max_length=255,
        description="University password"
    )
