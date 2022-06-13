import requests
import hashlib
import sys


# data = input("Enter your password: ")

def check_api(data_to_send):
    url = "https://api.pwnedpasswords.com/range/" + data_to_send
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"We encounter an error accessing this API. Error code is {response.status_code}")
    return response

def get_leaks(hashes, hashes_to_check):
    # Split the hashed result line in 2: hash and count
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hashes_to_check:
            return count
    return 0

def password_to_send(mypassword):
    sha1Pass = hashlib.sha1(mypassword.encode("utf-8")).hexdigest().upper()
    # Split first 5 letters from the rest
    first5, rest = sha1Pass[:5], sha1Pass[5:]
    # Calling the funtion for API request and parsing the firt 5 letters
    content = check_api(first5)
    # print(content)
    return get_leaks(content, rest)


def main(args):
    for password in args:
        count = password_to_send(password)
        if count:
            print(f"The password '{password}' was found {count} times!!")
        else:
            print(f"Your password is good for now!")

 


main(sys.argv[1:])
# password_to_send('qwerty')


