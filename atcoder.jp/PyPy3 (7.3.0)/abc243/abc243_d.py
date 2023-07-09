N, X = map(int,input().split())
S = list(input())

T = ['x']
for s in S:
    if s == 'U' and T[-1] in 'LR':
        T.pop()
    else:
        T.append(s)

for s in T[1:]:
    if s == 'U':
        X >>= 1
    elif s == 'L':
        X <<= 1
    else:
        X = (X << 1) + 1

print(X)