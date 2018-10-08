__author__ = "Geoffrey Bachelot"


def remove_odd_numbers(list):
    return [i for i in list if i % 2 == 0]


if __name == "__main__":
    original_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(remove_odd_numbers(original_list))
