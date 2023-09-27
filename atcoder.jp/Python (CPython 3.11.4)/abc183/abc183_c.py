from itertools import permutations

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for p in permutations(range(1, N), N - 1):
    s = T[0][p[0]]
    for i in range(N - 2):
        s += T[p[i]][p[i+1]]
    s += T[p[-1]][0]
    if s == K:
        ans += 1

print(ans)
