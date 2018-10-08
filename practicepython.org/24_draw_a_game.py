import time

__author__ = "Geoffrey Bachelot"


def create_grid_manual(size=3):
    horiz = " --- "
    vert = "|    "
    lines_lists = []
    vert_line = []

    # Build vertical lines
    while len(vert_line) < size + 1:
        vert_line.append(vert)
    # Remove trailing spaces from last char
    vert_line[-1] = str(vert_line[-1]).replace(' ', '')

    # Build list containing all lines
    drawn = 0
    while drawn < size:
        lines_lists.append(horiz * size)
        lines_lists.append(''.join(vert_line))
        drawn += 1
    lines_lists.append(horiz * size)  # Add the bottom line

    grid = '\n'.join(lines_lists)  # Convert list to grid

    return (grid)


def create_grid_clever(size=3):
    horiz = " ----"
    vert = "|    "
    vert_line = "\n"+vert*size+"|\n"
    horiz_line = [horiz*size]*(size+1)
    return vert_line.join(horiz_line)


if __name__ == "__main__":
    user_want = int(input('Grid size? ') or 3)
    start = time.time()
    print(create_grid_clever(user_want))
    end = time.time()
    print(end - start)
