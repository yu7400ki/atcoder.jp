H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        count_around = 0
        if S[i][j] == "#":
            continue
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= i + y < H and 0 <= j + x < W:
                if S[i + y][j + x] == "#":
                    count_around += 1
        if count_around > 1:
            print(i + 1, j + 1)
            exit()
