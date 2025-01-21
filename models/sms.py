from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import BaseModel


class SMS(BaseModel):
    """ Data class for SMS messages. """
    __tablename__ = "sms"

    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str] = mapped_column(String(160), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="completed_sms")

    def __repr__(self):
        return f"<SMS id={self.id} message={self.message} created_at={self.created_at}>"