import hashlib
from getpass import getpass
import requests


def check_password_safety(text):
    password_plain = text
    password_hashed = hashlib.sha1((password_plain).encode('utf-8')).hexdigest().upper()
    get_request_string = 'https://api.pwnedpasswords.com/range/' + password_hashed[0:5]
    r = requests.get(get_request_string)

    password_hashed_leftover = password_hashed[5:]
    if (r.text.find(password_hashed_leftover) == -1 and len(password_plain) > 8):
        return("The password appears to be safe")
    elif (r.text.find(password_hashed_leftover) == -1):
        return("Password seems to be secure but too short")
    else:
        return("The password is not secure!!")
