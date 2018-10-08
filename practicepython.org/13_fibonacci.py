__author__ = "Geoffrey Bachelot"


def fibonacci(amount: int):
    out = [1]
    while len(out) < amount:
        out.append(out[-1] + out[-1])

    return out

if __name__ == "__main__":
    choice = int(input('Choose fibonacci length: '))
    print(fibonacci(choice))
