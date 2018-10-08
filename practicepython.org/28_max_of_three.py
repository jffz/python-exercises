__author__ = "Geoffrey Bachelot"


def find_max(a, b, c):
    max = None
    if a > b:
        if a > c:
            max = a
        else:
            max = c
    else:
        if b > c:
            max = b
        else:
            max = c
    return max

if __name__ == "__main__":
    print(find_max(100, 5, 20))
