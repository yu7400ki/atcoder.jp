N, M = map(int, input().split())
X = list(map(int, input().split()))

acc = [0] * (N + 1)
length = 0

for x1, x2 in zip(X, X[1:]):
    s = min(x1, x2) - 1
    t = max(x1, x2) - 1
    d = t - s
    if d < N - d:
        acc[s] += N - 2 * d
        acc[t] -= N - 2 * d
    elif d > N - d:
        d = N - d
        acc[0] += N - 2 * d
        acc[s] -= N - 2 * d
        acc[t] += N - 2 * d
        acc[N] -= N - 2 * d
    length += d

for i in range(N):
    acc[i + 1] += acc[i]
acc.pop()

print(length + min(acc))
