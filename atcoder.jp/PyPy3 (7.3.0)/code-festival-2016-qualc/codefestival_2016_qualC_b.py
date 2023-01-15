N, T = map(int, input().split())
A = list(map(int, input().split()))

ma = max(A)
ans = max(ma * 2 - N - 1, 0)

print(ans)
