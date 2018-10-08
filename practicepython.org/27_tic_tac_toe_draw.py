import random
from check_tic_tac_toe import check_grid

__author__ = "Geoffrey Bachelot"


def case_free(grid, row, column):
    """Check if the desired case is free in the grid"""
    return grid[row][column] == 0


def random_choice(grid):
    r = random.randint(0, 2)
    c = random.randint(0, 2)
    return r, c


def choose_case():
    row, col = input('Choose a case ').split(',')
    return int(row) - 1, int(col) - 1


def tic_tac_toe():
    """
    Player1 = X
    Player2 = O
    """

    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    player = 1

    while check_grid(grid) == 0:
        print(*grid, sep='\n')

        # P1
        while True:
            if player != 1:
                p, c = random_choice(grid)
            else:
                p, c = choose_case()

            if case_free(grid, p, c):
                break
            else:
                print(f'Case already taken. ({p, c})')

        print('\n')
        grid[p][c] = player
        player = 3 - player

    else:
        print(*grid, sep='\n')
        print('-' * 21)
        print(f'Player {check_grid(grid)} won the game')
        print('-' * 21)


if __name__ == "__main__":
    rules = ("Please input your choice in the following format: row, column.\n"
             "Row and column are a number between 1 and 3.")
    print(rules)

    tic_tac_toe()
