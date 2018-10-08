__author__ = "Geoffrey Bachelot"


def age_in_100years():
    age = int(input('How old are you ?'))
    name = input('What\'s your name ?')
    repeat = int(input("Repeat count?"))

    for i in range(repeat):
        print(
            f"{name.capitalize()}, you will be {age + 100} in 100 years.",
            end='\n'
        )

if __name__ == "__main__":
    age_in_100years()