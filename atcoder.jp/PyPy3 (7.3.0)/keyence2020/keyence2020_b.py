N = int(input())
XL = [tuple(map(int, input().split())) for _ in range(N)]
ST = [(x - l, x + l) for x, l in XL]

ST.sort(key = lambda x: x[1])
arm = ST[0][1]
ans = 1

for i in range(1, N):
    if ST[i][0] >= arm:
        ans += 1
        arm = ST[i][1]

print(ans)
