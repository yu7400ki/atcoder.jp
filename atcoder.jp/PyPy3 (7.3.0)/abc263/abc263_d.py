N, L, R = map(int,input().split())
A = list(map(int,input().split()))

SUM = sum(A)
L_memo = [0]*(N+1)
R_memo = [0]*(N+1)

for i in range(N):
    L_memo[i+1] = L_memo[i] + L - A[i]
    R_memo[N-i-1] = R_memo[N-i] + R - A[N-i-1]
    #R_memo[i+1] = R_memo[i] + R - A[N-i-1]


mi = R_memo[-1]
for i in range(N, -1, -1):
    if R_memo[i] < mi:
        mi = R_memo[i]
    else:
        R_memo[i] = mi

mi = 0
for i in range(N+1):
    temp = L_memo[i] + R_memo[i]
    if temp < mi:
        mi = temp

print(SUM + mi)
