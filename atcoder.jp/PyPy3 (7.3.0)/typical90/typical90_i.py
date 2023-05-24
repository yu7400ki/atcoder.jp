import math
from bisect import bisect_left

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

def calc_slope_deg(x1, y1, x2, y2):
    deg = math.degrees(math.atan2(y2 - y1, x2 - x1))
    if deg < 0:
        deg += 360
    return deg

def deg_diff(deg1, deg2):
    diff = abs(deg1 - deg2)
    return min(diff, 360 - diff)

ans = 0
for j in range(N):
    slopes = []
    for i in range(N):
        if j == i:
            continue
        x1, y1 = XY[j]
        x2, y2 = XY[i]
        slopes.append(calc_slope_deg(x1, y1, x2, y2))
    slopes.sort()
    for deg in slopes:
        idx = bisect_left(slopes, (deg + 180) % 360)
        idx = min(idx, len(slopes) - 1)
        deg1 = deg_diff(deg, slopes[idx])
        idx = max(idx - 1, 0)
        deg2 = deg_diff(deg, slopes[idx])
        ans = max(ans, deg1, deg2)

print(ans)
