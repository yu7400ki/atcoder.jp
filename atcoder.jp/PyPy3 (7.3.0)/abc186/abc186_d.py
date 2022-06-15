N = int(input())
A = list(map(int,input().split()))
A.sort()

A_accum = [0]
for i in range(N):
    A_accum.append(A_accum[-1] + A[i])

ans = 0
for i in range(N-1):
    ans += abs(A[i] * (N-i-1) - (A_accum[-1] - A_accum[i+1]))

print(ans)