N, M = map(int, input().split())
A = set(map(lambda x: int(x) - 1, input().split()))

ans = [0] * N

for i in range(N - 1, -1, -1):
    if i in A:
        ans[i] = 0
    else:
        ans[i] = ans[i + 1] + 1

for i in range(N):
    print(ans[i])
