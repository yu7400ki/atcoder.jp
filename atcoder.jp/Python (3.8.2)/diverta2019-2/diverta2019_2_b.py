from itertools import permutations

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

ans = 1 << 60
for p in permutations(XY, 2):
    x1, y1 = p[0]
    x2, y2 = p[1]
    d1 = x2 - x1, y2 - y1

    cnt = 0
    for x3, y3 in XY:
        for x4, y4 in XY:
            d2 = x4 - x3, y4 - y3
            if d1 == d2:
                cnt += 1
                break

    ans = min(ans, N - cnt)

print(ans)
