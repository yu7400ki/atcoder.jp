N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)

acc = [0] * (N + 1)
for i in range(N):
    acc[i + 1] = acc[i] + F[i]

ans = float("inf")
i = 0
while True:
    x = i * P
    n = i * D
    tmp = acc[N] - acc[min(n, N)] + x
    ans = min(ans, tmp)
    i += 1
    if n >= N:
        break

print(ans)
