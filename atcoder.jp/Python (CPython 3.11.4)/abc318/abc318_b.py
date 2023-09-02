N = int(input())

sheet = [[0] * 100 for _ in range(100)]

for _ in range(N):
    X1, X2, Y1, Y2 = map(int, input().split())
    for i in range(Y1, Y2):
        for j in range(X1, X2):
            sheet[i][j] += 1

ans = 0
for i in range(100):
    for j in range(100):
        if sheet[i][j] > 0:
            ans += 1

print(ans)
