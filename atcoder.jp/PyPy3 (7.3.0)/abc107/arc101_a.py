N, K = map(int, input().split())
X = list(map(int, input().split()))

positive = [x for x in X if x >= 0]
negative = ([abs(x) for x in X[::-1] if x < 0])
ans = float('inf')

for p in range(K + 1):
    n = K - p

    if p == 0:
        if n - 1 < len(negative):
            ans = min(ans, negative[n - 1])
        continue
    elif n == 0:
        if p - 1 < len(positive):
            ans = min(ans, positive[p - 1])
        continue

    p -= 1
    n -= 1

    if p >= len(positive) or n >= len(negative):
        continue

    r = positive[p]
    l = negative[n]
    ans = min(ans, min(r, l) * 2 + max(r, l))

print(ans)
