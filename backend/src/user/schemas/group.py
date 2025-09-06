from pydantic import Field, EmailStr

from src.core.schemas import BaseSchema


class CreateGroupRequestSchema(BaseSchema):
    name: str = Field(
        ...,
        min_length=5,
        max_length=255,
        description="Group name"
    )
