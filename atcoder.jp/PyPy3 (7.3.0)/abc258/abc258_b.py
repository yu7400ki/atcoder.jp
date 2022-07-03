N = int(input())
A = [list(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        res1 = []
        res2 = []
        res3 = []
        res4 = []
        for k in range(N):
            res1.append(A[i][(j+k)%N])
            res2.append(A[(i+k)%N][j])
            res3.append(A[(i+k)%N][(j+k)%N])
            res4.append(A[(i-k)%N][(j+k)%N])
        ans = max(ans, int(''.join(res1)), int(''.join(res2)), int(''.join(res3)), int(''.join(res4)))

print(ans)