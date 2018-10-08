import random

__author__ = "Geoffrey Bachelot"


def find_cows(answer: int, guess: int):
    cows = 0
    str_answer = str(answer)
    for i in range(len(str_answer)):
        if str_answer[i] == str(guess)[i]:
            cows += 1
    return cows


def find_bulls(answer: int, guess: int, cows: int):
    bulls = 0
    for i in str(guess):
        if i in str(answer):
            bulls += 1
    return bulls - cows


def game(cheat=False):
    answer = random.randint(1000, 10000)
    triies = 1

    if cheat is True:
        print(answer)

    while True:
        guess = int(input('Pick a 4 digits number: '))
        cows = find_cows(answer, guess)
        bulls = find_bulls(answer, guess, cows)

        if guess == answer:
            print(f'You won with {triies} triies!')
            break
        else:
            print(f'{cows} cows, {bulls} bulls')
            triies += 1
            continue

if __name__ == "__main__":
    game(cheat=True)
