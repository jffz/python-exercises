__author__ = "Geoffrey Bachelot"


def is_palindrome(string):
    return string == string[::-1]


if __name__ == "__main__":
    user_input = input("Input your string: ")

    if is_palindrome(user_input):
        print(f'{user_input} is a palindrome.')
    else:
        print('Nope!')