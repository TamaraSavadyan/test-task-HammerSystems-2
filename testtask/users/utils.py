import re
from random import randint
from string import ascii_letters, digits
from secrets import choice


def generate_invite_code():
    alphabet = ascii_letters + digits
    return ''.join(choice(alphabet) for _ in range(6))

def generate_auth_code():
    return randint(1000, 9999)


phone_pattern = (
    r"^(\+\d{1,3}\s?)?(\d{3}|(\(\d{3}\)))?[\s.-]?\d{3}[\s.-]?\d{2}[\s.-]?\d{2}$"
)
phone_regex = re.compile(phone_pattern)


def validate_phone_number(phone_number):
    if phone_regex.match(phone_number):
        return True
    else:
        return False
