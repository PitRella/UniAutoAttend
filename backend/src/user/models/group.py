from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from .user import User
from src.core.mixins import PrimaryKeyMixin, TimeStampMixin


class Group(PrimaryKeyMixin, TimeStampMixin):
    __tablename__ = 'groups'

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
        comment="Group name"
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
        comment="Group description"
    )

    users: Mapped[list["User"]] = relationship(
        "User",
        back_populates="group",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f'<Group(id={self.id}, name="{self.name}")>'
