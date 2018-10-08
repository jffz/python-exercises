import random

__author__ = "Geoffrey Bachelot"


def guessing():
    answer = random.randint(1, 9)
    guessing = None

    while guessing != answer:
        guessing = int(input('Guess the number: '))
        if guessing > answer:
            print(f'You picked {guessing}, too high.')
        elif guessing < answer:
            print(f'You picked {guessing}, too low.')
        else:
            print('You won!')
            break


if __name__ == "__main__":
    guessing()
