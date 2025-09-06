from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.sql.schema import UniqueConstraint

from src.core.mixins import PrimaryKeyMixin, TimeStampMixin


class User(PrimaryKeyMixin, TimeStampMixin):
    __tablename__ = 'users'

    telegram_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        unique=True,
        index=True,
        comment="Telegram user ID"
    )

    username: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        comment="Telegram username"

    )
    university_email: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    university_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        comment="Is active?"
    )

    __table_args__ = (
        UniqueConstraint(
            "telegram_id",
            name="uq_telegram_users_tg_id"
        ),
    )

    def __repr__(self) -> str:
        return f'<TelegramUser(tg_id={self.telegram_id}, username="{self.username}")>'
