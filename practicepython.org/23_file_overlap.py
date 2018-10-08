import json
import os
from divisors import get_divisors
from prime_numbers import is_prime

__author__ = "Geoffrey Bachelot"


def create_file_with_content(filename, data):
    if not os.path.exists(filename):
        with open(filename, 'w') as openfile:
            openfile.write(data)


def gen_prime_list(maxnumber=1000):
    primes = []
    for i in range(1, maxnumber + 1):
        if is_prime(i):
            primes.append(i)
    return primes


if __name__ == "__main__":
    files_and_data = {
        'prime.txt': json.dumps(gen_prime_list()),
        'fancy.txt': json.dumps(list(range(1, 1001)))
    }

    for k, v in files_and_data.items():
        create_file_with_content(k, v)

    
