import os
from datetime import datetime
from typing import Type

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

from models.user import User
from models.sms import SMS


if not os.path.exists("data/"):
    os.makedirs("data/")
engine = create_engine("sqlite:///data/db.sqlite")
User.metadata.create_all(engine)
SMS.metadata.create_all(engine)


def create_user(phone_number: int) -> User:
    """ Create a user with the given phone number. """
    with Session(engine) as session:
        user = User(phone_number=phone_number)
        session.add(user)
        session.commit()
        return user


def get_user_by_id(user_id: int) -> User:
    """ Get a user by their ID. """
    with Session(engine) as session:
        return session.query(User).get(user_id)


def get_user(phone_number: int) -> User:
    """
    Get a user by their phone number.
    Create a new user if one does not exist.
    """
    with Session(engine) as session:
        user = session.query(User).filter_by(phone_number=phone_number).first()
        if user is None:
            user = create_user(phone_number)
        return user


def add_completed_sms_to_user(user: User, message: str, created_at: datetime) -> SMS:
    """ Add an SMS message to a user. """
    with Session(engine) as session:
        sms = SMS(message=message, created_at=created_at, user=user)
        session.add(sms)
        session.commit()
        return sms


def get_completed_sms_by_number(phone_number: int) -> list[Type[SMS]]:
    """ Get all completed SMS messages for a user by their phone number. """
    with Session(engine) as session:
        user = get_user(phone_number)
        return session.query(SMS).filter_by(user=user).all()


if __name__ == "__main__":
    user = get_user(1234567890)
    add_completed_sms_to_user(user, "Hello, World!", datetime.now())
    print(get_completed_sms_by_number(1234567890))