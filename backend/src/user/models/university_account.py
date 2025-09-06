from sqlalchemy import String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.mixins import TimeStampMixin, PrimaryKeyMixin
from src.user.enum import UniversityTypeEnum
from src.user.models import User


class UniversityAccount(PrimaryKeyMixin, TimeStampMixin):
    __tablename__ = "university_accounts"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )
    user: Mapped["User"] = relationship(
        "TelegramUser",
        back_populates="university_accounts"
    )
    university_type: Mapped[UniversityTypeEnum] = mapped_column(
        Enum(UniversityTypeEnum),
        nullable=False
    )
    university_email: Mapped[str] = mapped_column(String(255), nullable=False)
    university_password: Mapped[str] = mapped_column(
        "uni_password",
        String(255),
        nullable=False
    )

    def __repr__(self) -> str:
        return f"<UniversityAccount(type={self.university_type}, email={self.university_email})>"
