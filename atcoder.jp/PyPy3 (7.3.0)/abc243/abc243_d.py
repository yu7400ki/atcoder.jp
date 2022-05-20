N, X = map(int,input().split())
S = list(input())

for s in S:
    if s == 'U':
        X //= 2
    elif s == 'L':
        X *= 2
    else:
        X = X * 2 + 1

print(X)