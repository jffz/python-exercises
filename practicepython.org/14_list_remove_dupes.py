__author__ = "Geoffrey Bachelot"


def remove_dupes(data: list):
    return list(set(data))

if __name__ == "__main__":
    original_list = [1, 1, 2, 3, 5, 8, 8, 13, 13, 21, 34, 55, 89]
    print(remove_dupes(original_list))
