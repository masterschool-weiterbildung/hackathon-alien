import time

import db
from db import *
from sqlalchemy.orm import close_all_sessions
from sqlalchemy import text
import pytest


def release_locks():
    with db.engine.connect() as conn:
        conn.execute(text("PRAGMA busy_timeout = 0;"))  # Fail immediately if locked
        conn.execute(text("PRAGMA wal_checkpoint(TRUNCATE);"))  # Clear WAL state


@pytest.fixture(scope="function")
def testing_db_setup():
    db_file = "test_db.sqlite"
    database_setup(db_file)

    yield

    close_all_sessions()
    release_locks()
    db.engine.dispose()

    time.sleep(0.1)

    if os.path.exists(f"data/{db_file}"):
        os.remove(f"data/{db_file}")



def test_create_user(testing_db_setup):
    user = create_user(1234567890)
    assert user.phone_number == 1234567890


def test_get_user_by_id(testing_db_setup):
    user = create_user(1234567890)
    assert get_user_by_id(user.id) == user


def test_get_user(testing_db_setup):
    user = get_user(1234567890)
    assert user.phone_number == 1234567890
    assert get_user(1234567890) == user


def test_add_completed_sms_to_user(testing_db_setup):
    user = get_user(1234567890)
    sms = add_completed_sms_to_user(user, "Hello, World!", datetime.now())
    assert sms.message == "Hello, World!"
    assert sms.user.id == user.id


def test_get_completed_sms_by_number(testing_db_setup):
    user = get_user(1234567890)
    sms = add_completed_sms_to_user(user, "Hello, World!", datetime.now())
    assert get_completed_sms_by_number(1234567890) == [sms]

    user2 = get_user(9876543210)
    sms2 = add_completed_sms_to_user(user2, "Goodbye, World!", datetime.now())
    assert get_completed_sms_by_number(9876543210) == [sms2]
    assert get_completed_sms_by_number(1234567890) == [sms]