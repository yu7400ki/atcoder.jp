N = int(input())
W = []
X = []

for i in range(N):
    w, x = map(int, input().split())
    W.append(w)
    X.append(x)

ans = 0
for i in range(24):
    tmp = 0
    for j in range(N):
        w = W[j]
        x = (X[j] + i) % 24
        if 9 <= x <= 17:
            tmp += w
    ans = max(ans, tmp)

print(ans)
