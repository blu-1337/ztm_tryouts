# to use this program you need to run in the command line:
# python checkmypass.py yourPassword anotherPassword andSoOnPassword
# it will return all passwords security checks

import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:  # if the status is not OK
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):  # check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]  # get the first 5 characters and then the tail
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should change your password')
        else:
            print(f'{password} was not found. Carry on!')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))  # sys.exit() makes sure that it exits

