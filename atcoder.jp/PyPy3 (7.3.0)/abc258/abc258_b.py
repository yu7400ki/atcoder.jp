N = int(input())
A = [list(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        res = []
        for k in range(N):
            res.append(A[i][(j+k)%N])
        ans = max(ans, int(''.join(res)))
        ans = max(ans, int(''.join(reversed(res))))
        res = []
        for k in range(N):
            res.append(A[(i+k)%N][j])
        ans = max(ans, int(''.join(res)))
        ans = max(ans, int(''.join(reversed(res))))
        res = []
        for k in range(N):
            res.append(A[(i+k)%N][(j+k)%N])
        ans = max(ans, int(''.join(res)))
        ans = max(ans, int(''.join(reversed(res))))
        res = []
        for k in range(N):
            res.append(A[(i-k)%N][(j+k)%N])
        ans = max(ans, int(''.join(res)))
        ans = max(ans, int(''.join(reversed(res))))

print(ans)