N, X = map(int,input().split())
S = list(input())

T = [1]
for s in S:
    if s == 'U' and T[-1] in 'LR':
        T.pop()
    else:
        T.append(s)

for s in T[1:]:
    if s == 'U':
        X //= 2
    elif s == 'L':
        X *= 2
    else:
        X = X * 2 + 1

print(X)