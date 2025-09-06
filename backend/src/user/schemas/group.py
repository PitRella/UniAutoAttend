from pydantic import Field, EmailStr

from src.core.schemas import BaseSchema


class CreateGroupRequestSchema(BaseSchema):
    telegram_id: int = Field(
        ...,
        ge=0,
        description="Telegram ID"
    )
    name: str = Field(
        ...,
        min_length=5,
        max_length=255,
        description="Group name"
    )
