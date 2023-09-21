N, T = map(int, input().split())

ans = 1e10
for _ in range(N):
    c, t = map(int, input().split())
    if t <= T:
        ans = min(ans, c)

if ans == 1e10:
    print("TLE")
else:
    print(ans)
