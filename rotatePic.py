grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['0', '0', '0', '0', '0', '.'],
    ['.', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]


def rotatePicClockwise(pic):
    for item in range(len(pic[0])):  # for item in first line
        for line in range(len(pic)):  # for line in image
            print(pic[line][item], end='')
        print()

rotatePicClockwise(grid)
