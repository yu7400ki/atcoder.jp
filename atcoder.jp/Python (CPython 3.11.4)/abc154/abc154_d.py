N, K = map(int, input().split())
P = list(map(int, input().split()))

def exp(p):
    return (1 + p) / 2

P = [exp(p) for p in P]
acc = [0] * (N + 1)
for i in range(N):
    acc[i + 1] = acc[i] + P[i]

ans = 0
for i in range(N - K + 1):
    ans = max(ans, acc[i + K] - acc[i])

print(ans)
