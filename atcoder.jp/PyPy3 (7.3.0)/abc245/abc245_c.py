N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dp = [None] * (N+1)
ep = [None] * (N+1)
dp[1] = ep[1] = True

for i in range(2,N+1):
    if abs(A[i-2] - A[i-1]) <= K:
        dp[i] = True
    elif abs(B[i-2] - A[i-1]) <= K:
        dp[i] = True
    else:
        dp[i] = False
    if abs(A[i-2] - B[i-1]) <= K:
        ep[i] = True
    elif abs(B[i-2] - A[i-1]) <= K:
        ep[i] = True
    else:
        ep[i] = False
    if not dp[i] and not ep[i]:
        print('No')
        exit()

print('Yes')