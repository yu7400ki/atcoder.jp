A = [list(map(int, input().split())) for _ in range(9)]

def is_valid_sudoku(board):
    for row in board:
        if not is_valid_row(row):
            return False

    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_row(column):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_row(block):
                return False

    return True

def is_valid_row(row):
    digits = set()
    for num in row:
        if num == ".":
            continue
        if num in digits:
            return False
        digits.add(num)
    return True

print("Yes" if is_valid_sudoku(A) else "No")
