import uuid
from datetime import datetime, timedelta
from django.utils import timezone


def get_random_code():
    """
    The function `random_code` generates a random code with 12 chars using the UUID library in Python.
    :return: The code is returning the last part of a randomly generated UUID.
    """
    return str(uuid.uuid4()).split("-")[-1]

def get_default_expected_delivery_date():
    return timezone.now() + timedelta(days=3)