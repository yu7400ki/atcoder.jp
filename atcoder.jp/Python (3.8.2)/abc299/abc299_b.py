N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

if T not in C:
    T = C[0]

res = -1
ans = None
for i in range(N):
    if C[i] == T:
        if res < R[i]:
            res = R[i]
            ans = i + 1

print(ans)