X, K = map(int,input().split())

def round(x, k):
    x_ = x / 10**(k + 1)
    x_ = int(x_ + 0.5)
    return x_ * 10**(k+1)

for i in range(K):
    X = round(X, i)

print(X)