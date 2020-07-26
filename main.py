import hashlib
from getpass import getpass
import requests


print("Welcome to IsYourPasswordSafe")
password_plain = getpass("Please enter your password \n")
password_hashed = hashlib.sha1((password_plain).encode('utf-8')).hexdigest().upper()
get_request_string = 'https://api.pwnedpasswords.com/range/' + password_hashed[0:5]
r = requests.get(get_request_string)

password_hashed_leftover = password_hashed[5:]
if (r.text.find(password_hashed_leftover) > -1 ):
    print("\nPassword has already been leaked and not safe")
else:
    print("\nThe password appears to be safe")

wait = input("Press any button to leave the Program")
