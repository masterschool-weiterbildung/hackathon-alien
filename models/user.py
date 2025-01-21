from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import BaseModel


class User(BaseModel):
    """ Data class for users. """
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    phone_number: Mapped[int] = mapped_column(nullable=False)

    completed_sms: Mapped[List["SMS"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User id={self.id} phone_number={self.phone_number}>"

    def __eq__(self, other):
        return self.id == other.id and self.phone_number == other.phone_number