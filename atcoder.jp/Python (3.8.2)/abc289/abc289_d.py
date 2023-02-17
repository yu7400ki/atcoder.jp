N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
X = int(input())

dp = [False] * (X + 1)
dp[0] = True

for i in range(X):
    if not dp[i]:
        continue

    for a in A:
        pos = i + a
        if pos <= X and pos not in B:
            dp[pos] = True

if dp[X]:
    print('Yes')
else:
    print('No')
