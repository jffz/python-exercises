__author__ = "Geoffrey Bachelot"


def first_and_last(datas: list):
    return [datas[0], datas[-1]]

if __name__ == "__main__":
    mylist = [1, 2, 4, 8, 55, 72, 42]
    print(first_and_last(mylist))