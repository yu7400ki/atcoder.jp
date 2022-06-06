N = int(input())
xy = [tuple(map(int,input().split())) for _ in range(N)]

ans = -1
for i in range(N):
    for j in range(i+1, N):
        x = (xy[i][0] - xy[j][0]) ** 2
        y = (xy[i][1] - xy[j][1]) ** 2
        ans = max(ans, x+y)

print(ans**0.5)