from divisors import get_divisors

__author__ = "Geoffrey Bachelot"


def is_prime(number):
    return get_divisors(number) == [1, number]

if __name__ == "__main__":
    number = int(input("Number: "))
    print(f'Is number {number} prime: {is_prime(number)}')
