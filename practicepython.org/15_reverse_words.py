__author__ = "Geoffrey Bachelot"


def reverse(string):
    return ' '.join(string.split(' ')[::-1])

if __name__ == "__main__":
    print(reverse(input('Write me something please: ')))
