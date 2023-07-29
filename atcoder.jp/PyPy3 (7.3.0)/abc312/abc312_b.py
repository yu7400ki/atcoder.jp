def check_pattern(array):
    if not all(array[i][j] == "#" for i in range(3) for j in range(3)):
        return False

    if not all(array[i][j] == "#" for i in range(6, 9) for j in range(6, 9)):
        return False
    
    pattern = [
        ["#", "#", "#", "."],
        ["#", "#", "#", "."],
        ["#", "#", "#", "."],
        [".", ".", ".", "."],
    ]

    for i in range(4):
        for j in range(4):
            if array[i][j] != pattern[i][j]:
                return False

    pattern = [
        [".", ".", ".", "."],
        [".", "#", "#", "#"],
        [".", "#", "#", "#"],
        [".", "#", "#", "#"],
    ]

    for i in range(4):
        for j in range(4):
            if array[i+5][j+5] != pattern[i][j]:
                return False

    return True


N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

for i in range(N - 8):
    for j in range(M - 8):
        subarray = [row[j:j + 9] for row in S[i:i + 9]]
        if check_pattern(subarray):
            print(i+1, j+1)
