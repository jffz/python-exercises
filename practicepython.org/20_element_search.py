import random

__author__ = "Geoffrey Bachelot"


def create_list(length=10, max_int=100):
    foo = set()
    while len(foo) < length:
        foo.add(random.randint(1, max_int))
    return list(foo)


def element_search(mylist, search):
    return search in mylist

if __name__ == "__main__":
    user_input = int(input('Pick a number: '))

    print(element_search(create_list(), user_input))
