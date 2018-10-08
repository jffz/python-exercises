__author__ = "Geoffrey Bachelot"


def get_divisors(number):
    """Return the divisors of a number"""
    divisors = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)

    return divisors

if __name__ == "__main__":
    number = int(input("Number: "))
    print(get_divisors(number))
