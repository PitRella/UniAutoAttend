from pydantic import BaseModel, Field


class CreateUserRequestSchema(BaseModel):
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

