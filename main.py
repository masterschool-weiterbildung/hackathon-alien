from datetime import datetime
import time

from api import SMSAPI
from db import get_user, database_setup, add_completed_sms_to_user
from fetch_romulan_dict import english_to_romulan
from menu import show_menu, process_selection
from utility import TEAM_NAME

sms_api = SMSAPI()


def parse_timestamp(timestamp: str) -> datetime:
    """ takes timestamp as input & outputs datetime object """
    formats = [
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S.%f%z",
    ]
    for fmt in formats:
        try:
            return datetime.strptime(timestamp, fmt)
        except ValueError:
            continue
    raise ValueError(f"Timestamp '{timestamp}' does not match any supported formats.")


def format_timestamp(timestamp: datetime or str) -> str:
    """ takes the datetime object and returns the formatted timestamp """
    if isinstance(timestamp, datetime):
        return timestamp.isoformat()  # Convert datetime to ISO 8601 string
    return timestamp  # If it's already a string, return as is


def get_new_messages() -> list[dict]:
    """
    fetches all SMS API messages and checks if they are present in DB
    outputs list of new messages
    """
    new_messages = []
    messages = sms_api.get_messages(TEAM_NAME)

    for number, number_messages in messages.items():
        user = get_user(number)
        completed_messages = user.completed_sms

        # Extract completed messages as a set of tuples (text and rounded datetime)
        completed_messages_set = {
            (completed_message.message, format_timestamp(completed_message.created_at))
            for completed_message in completed_messages
        }

        for message in number_messages:
            message_datetime = format_timestamp(message["receivedAt"])
            message_text = message["text"]

            duplicate = False
            for completed_message_text, completed_message_datetime in completed_messages_set:
                if message_text == completed_message_text:
                    reformatted_message_datetime = parse_timestamp(message_datetime).replace(tzinfo=None)
                    reformatted_completed_message_datetime = parse_timestamp(completed_message_datetime).replace(tzinfo=None)
                    if reformatted_message_datetime == reformatted_completed_message_datetime:
                        duplicate = True
            if not duplicate:
                print(f"Got new message from {number}: {message_text}")
                new_messages.append({"number": number, "message": message})

    return new_messages


def main_loop() -> None:
    """ main_loop that regularly checks for new messages and handles them """
    while True:
        new_messages = get_new_messages()
        for message_dict in new_messages:
            number = message_dict["number"]
            message = message_dict["message"]
            if message["text"].lower() == "Help!".lower():
                show_menu(number)
            elif message["text"].isdigit():
                process_selection(number, message["text"])
            elif message["text"].lower().startswith("romulan"):
                text = message["text"][8:]
                sms_api.send_sms(number, english_to_romulan(text))
            user = get_user(number)
            add_completed_sms_to_user(user, message["text"], datetime.strptime(message["receivedAt"], "%Y-%m-%dT%H:%M:%S.%f%z"))
        time.sleep(10)


def main():
    database_setup()
    main_loop()


if __name__ == '__main__':
    main()
