A, B = map(int, input().split())

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

def is_adjacent(grid, a, b):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == a:
                a_i, a_j = i, j
            if grid[i][j] == b:
                b_i, b_j = i, j
    if abs(a_i - b_i) + abs(a_j - b_j) == 1:
        return True
    else:
        return False

if is_adjacent(grid, A, B):
    print("Yes")
else:
    print("No")
