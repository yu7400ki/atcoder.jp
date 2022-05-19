N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dp = [False] * (N)
ep = [False] * (N)
dp[0] = ep[0] = True

for i in range(1,N):
    if dp[i-1]:
        if abs(A[i-1] - A[i]) <= K:
            dp[i] = True
        if abs(A[i-1] - B[i]) <= K:
            ep[i] = True
    if ep[i-1]:
        if abs(B[i-1] - A[i]) <= K:
            dp[i] = True
        if abs(B[i-1] - B[i]) <= K:
            ep[i] = True

if dp[-1] or ep[-1]:
    print('Yes')
else:
    print('No')