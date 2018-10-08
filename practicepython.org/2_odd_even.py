__author__ = "Geoffrey Bachelot"

number = int(input("Pick a number. "))
even = number % 2 == 0

if even:
    print("Your number is even")
else:
    print("Your number is odd")
