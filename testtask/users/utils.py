import random
import re


def generate_auth_code():
    return random.randint(1000, 9999)


phone_pattern = (
    r"^(\+\d{1,3}\s?)?(\d{3}|(\(\d{3}\)))?[\s.-]?\d{3}[\s.-]?\d{2}[\s.-]?\d{2}$"
)
phone_regex = re.compile(phone_pattern)


def validate_phone_number(phone_number):
    if phone_regex.match(phone_number):
        return True
    else:
        return False
