import pygame as pg

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(boa):
    for row in range(len(boa)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")

        for col in range(len(boa[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")

            if col == 8:
                print(boa[row][col])
            else:
                print(str(boa[row][col]) + " ", end="")


def find_empty(boa):
    for row in range(len(boa)):
        for col in range(len(boa[0])):
            if boa[row][col] == 0:
                return (row, col)  # return row, col of empty space as a tuple

    return None


def is_valid(boa, num, pos):
    # Check row
    for col in range(len(boa[0])):
        if boa[pos[0]][col] == num and pos[1] != col:
            return False
    # Check column
    for row in range(len(boa)):
        if boa[row][pos[1]] == num and pos[0] != row:
            return False

    # Check box
    box_col = pos[1] // 3
    box_row = pos[0] // 3

    for row in range(box_row * 3, box_row * 3 + 3):
        for col in range(box_col * 3, box_col * 3 + 3):
            if boa[row][col] == num and (row, col) != pos:
                return False

    return True


def solve(boa):
    is_full = find_empty(boa)  # is_full is a tuple that if there is no empty space, it will return None
    if not is_full:
        return True  # if there is no empty space, the board is full and the game is over
    else:
        row, col = is_full

    for i in range(1, 10):
        if is_valid(boa, i, (row, col)):
            boa[row][col] = i

            if solve(boa):
                return True

            boa[row][col] = 0

print("Original board:")
print_board(board)
solve(board)
print("Solved board:")
print_board(board)
