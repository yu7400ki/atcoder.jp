N = int(input())

ans = 0

for r in range(1, int(N ** 0.5) + 1):
    if (N - r) % r == 0:
        m = (N - r) // r
        if r < m:
            ans += m

print(ans)
