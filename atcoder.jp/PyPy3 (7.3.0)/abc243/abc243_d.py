N, X = map(int,input().split())
S = list(input())

cnt = 0
for i in range(N):
    if S[i-cnt] == 'U':
        if S[i-1-cnt] == 'L' or S[i-1-cnt] == 'R':
            del S[i-cnt]
            del S[i-1-cnt]
            cnt += 2

for s in S:
    if s == 'U':
        X //= 2
    elif s == 'L':
        X *= 2
    else:
        X = X * 2 + 1

print(X)