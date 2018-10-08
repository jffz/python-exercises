import random

__author__ = "Geoffrey Bachelot"


def guess_number(number, min=0, max=100):
    triies = 1

    while True:
        guess = round((min + max) / 2)
        if guess < number:
            min = guess
        elif guess > number:
            max = guess
        else:
            break
        triies += 1

    print(f'My awesome bot found {guess} in {triies} triies.')


if __name__ == "__main__":
    guess_number(int(input('Nombre: ')), max=100000)
