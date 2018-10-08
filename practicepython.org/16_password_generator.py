import string
import random

__author__ = "Geoffrey Bachelot"


def gen_passwd(length=10):

    weak_passwd = [
        "weak",
        "123456",
        "password"
    ]

    if length == 0:
        return random.choice(weak_passwd)
    else:
        passwd = ""
        while len(passwd) < length:
            passwd = passwd + random.choice(string.printable[:-6])
        return passwd

if __name__ == "__main__":
    length = int(input('Password length (0 = weak) ? '))
    print(gen_passwd(length))
