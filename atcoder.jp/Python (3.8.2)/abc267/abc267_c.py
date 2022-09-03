N, M = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
for i in range(N-M+1):
    t = 0
    for j in range(M):
        t += A[j+i] * (j + 1)
    ans = max(ans, t)

print(ans)