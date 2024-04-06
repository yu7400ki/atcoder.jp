from collections import deque

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            s = (i, j)
            A[i][j] = "."
        if A[i][j] == "T":
            t = (i, j)
            A[i][j] = "."
E = [[0] * W for _ in range(H)]
N = int(input())
for _ in range(N):
    R, C, e = map(int, input().split())
    R -= 1
    C -= 1
    E[R][C] = e
inf = 1 << 60


def solve():
    energy = [[-inf] * W for _ in range(H)]
    used = [[False] * W for _ in range(H)]
    c = s
    q = deque([c])
    while q:
        i, j = q.popleft()
        if not used[i][j]:
            energy[i][j] = max(energy[i][j], E[i][j])
            used[i][j] = True
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if A[ni][nj] == "#":
                continue
            if energy[i][j] <= 0:
                continue
            if energy[ni][nj] < energy[i][j] - 1:
                energy[ni][nj] = energy[i][j] - 1
                q.append((ni, nj))
    return energy[t[0]][t[1]]


ans = solve()
if ans >= 0:
    print("Yes")
else:
    print("No")
