N, A, B = map(int, input().split())
X = list(map(int, input().split()))

ans = 0
pos = X[0]

for x in X:
    ans += min((x - pos) * A, B)
    pos = x

print(ans)
