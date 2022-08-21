X, Y, N = map(int,input().split())

n = N
cnt = n // 3
n -= cnt * 3

ans = min(cnt * Y + n * X, N * X)
print(ans)