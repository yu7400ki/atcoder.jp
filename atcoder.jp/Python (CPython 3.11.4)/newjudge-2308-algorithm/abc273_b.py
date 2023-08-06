X, K = map(int, input().split())

def round(x, k):
    x //= 10 ** k
    x += 5
    x //= 10
    x *= 10 ** (k + 1)
    return x

for k in range(K):
    X = round(X, k)

print(X)
