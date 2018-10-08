__author__ = "Geoffrey Bachelot"

original_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
limiter = int(input("Select a max number: "))

print([i for i in original_list if i < limiter])
