__auhtor__ = "Geoffrey Bachelot"


def check_grid(grid):
    """Return the playerid of tic tac toe winner"""

    for i in range(3):
        # rows
        row = set([grid[i][0], grid[i][1], grid[i][2]])
        if len(row) == 1 and grid[i][0] != 0:
            return grid[i][0]

        # Column win
        column = set([grid[0][i], grid[1][i], grid[2][i]])
        if len(column) == 1 and grid[0][i] != 0:
            return grid[0][i]

    # Diag win
    diag1 = set([grid[0][0], grid[1][1], grid[2][2]])
    diag2 = set([grid[0][2], grid[1][1], grid[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
        return grid[1][1]

    return 0


if __name__ == '__main__':
    game = [
        [1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]
    ]
    print(chech_grid(game))
