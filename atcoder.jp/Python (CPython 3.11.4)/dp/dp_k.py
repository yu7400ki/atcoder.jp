N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (K + 1)

for k in range(K, -1, -1):
    for a in A:
        if k - a >= 0:
            dp[k - a] |= not dp[k]

if dp[0]:
    print("First")
else:
    print("Second")
