N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

ans = 0

for s in S:
    for t in T:
        if s.endswith(t):
            ans += 1
            break

print(ans)
