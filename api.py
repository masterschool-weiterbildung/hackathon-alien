import threading
import requests

from queue import Queue
from ratelimit import limits, sleep_and_retry

from utility import RATE_LIMIT, SMS_API_URL, REGISTER_PHONE_TO_TEAM, \
    DEFAULT_NUMBER, TEAM_NAME, TEST_NUMBER, UNREGISTER_PHONE_TO_TEAM, \
    GET_MESSAGES, SEND_SMS


class SMSAPI():
    def __init__(self):
        pass

    @sleep_and_retry
    @limits(calls=RATE_LIMIT, period=1)
    def send_sms_to_register_phone_to_team(self, to_number, team_name):
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "phoneNumber": to_number,
            "teamName": team_name
        }

        try:
            response = requests.post(SMS_API_URL + REGISTER_PHONE_TO_TEAM,
                                     json=payload,
                                     headers=headers,
                                     verify=True,
                                     timeout=5)

            response.raise_for_status()

            if response.status_code == 200:
                return response.text

        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException
        except ValueError as e:
            raise ValueError

    @sleep_and_retry
    @limits(calls=RATE_LIMIT, period=1)
    def send_sms_to_unregister_phone_to_team(self, to_number, team_name):
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "phoneNumber": to_number,
            "teamName": team_name
        }

        try:
            response = requests.post(SMS_API_URL + UNREGISTER_PHONE_TO_TEAM,
                                     json=payload,
                                     headers=headers,
                                     verify=True,
                                     timeout=5)

            response.raise_for_status()

            if response.status_code == 200:
                return response.text

        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException
        except ValueError as e:
            raise ValueError

    @sleep_and_retry
    @limits(calls=RATE_LIMIT, period=1)
    def get_messages(self, team_name):
        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(SMS_API_URL + GET_MESSAGES + team_name,
                                    headers=headers,
                                    verify=True,
                                    timeout=5)

            response.raise_for_status()

            if response.status_code == 200:
                return response.json()

        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException
        except ValueError as e:
            raise ValueError

    @sleep_and_retry
    @limits(calls=RATE_LIMIT, period=1)
    def send_sms(self, to_number, message):
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "phoneNumber": to_number,
            "message": message
        }

        try:
            response = requests.post(SMS_API_URL + SEND_SMS,
                                     json=payload,
                                     headers=headers,
                                     verify=True,
                                     timeout=5)

            response.raise_for_status()

            if response.status_code == 200:
                return response.json()

        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException
        except ValueError as e:
            raise ValueError


def register_phone_to_team(numbers: list):
    # Queue for SMS tasks
    sms_queue = Queue()
    # Instantiate the SMSAPI Object
    sms_ap = SMSAPI()

    def worker():
        while True:
            task = sms_queue.get()
            if task is None:
                break
            to_number = task
            print(sms_ap.send_sms_to_register_phone_to_team(to_number,
                                                            TEAM_NAME))
            sms_queue.task_done()

    creates_threads(numbers, sms_queue, worker)


def unregister_phone_to_team(numbers: list):
    # Queue for SMS tasks
    sms_queue = Queue()
    # Instantiate the SMSAPI Object
    sms_ap = SMSAPI()

    def worker():
        while True:
            task = sms_queue.get()
            if task is None:
                break
            to_number = task
            print(sms_ap.send_sms_to_unregister_phone_to_team(to_number,
                                                              TEAM_NAME))
            sms_queue.task_done()

    creates_threads(numbers, sms_queue, worker)


def send_sms_number(numbers: list[dict]):
    # Queue for SMS tasks
    sms_queue = Queue()

    # Instantiate the SMSAPI Object
    sms_ap = SMSAPI()

    def worker():
        while True:
            task = sms_queue.get()
            if task is None:
                break
            to_number, message = task
            print(sms_ap.send_sms(to_number, message))

            sms_queue.task_done()

    return creates_threads_sending(numbers, sms_queue, worker)


def creates_threads_sending(numbers, sms_queue, worker):
    # Start worker threads
    for _ in range(len(numbers)):
        thread = threading.Thread(target=worker, daemon=True)
        thread.start()
    # Add SMS tasks to the queue

    for number_dict in numbers:
        for number, message in number_dict.items():
            sms_queue.put((number, message))

    # Wait for all messages to be processed
    sms_queue.join()


def creates_threads(numbers, sms_queue, worker):
    # Start worker threads
    for _ in range(len(numbers)):
        thread = threading.Thread(target=worker, daemon=True)
        thread.start()
    # Add SMS tasks to the queue
    for number in numbers:
        sms_queue.put((number))
    # Wait for all messages to be processed
    sms_queue.join()


def main():
    numbers = [DEFAULT_NUMBER]
    register_phone_to_team(numbers)


if __name__ == '__main__':
    main()
