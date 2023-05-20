from collections import namedtuple
from math import atan2, degrees

Point = namedtuple('Point', ['x', 'y'])

N = int(input())
XY = [Point(*map(int, input().split())) for _ in range(N)]


def calc_slope(point1, point2):
    deg =  degrees(atan2(point2.y - point1.y, point2.x - point1.x))
    return deg if deg >= 0 else 360 + deg


def deg_diff(deg1, deg2):
    diff = abs(deg1 - deg2)
    return min(diff, 360 - diff)


def binary_search(lst, target, ok = -1, ng = None, key = None):
    ng = len(lst) if ng is None else ng
    key = (lambda x: lst[x] <= target) if key is None else key

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if key(mid):
            ok = mid
        else:
            ng = mid

    return ok


ans = 0
for p_j in XY:
    slopes_dict = {}
    for p_i in XY:
        if p_i == p_j:
            continue
        slopes_dict[p_i] = calc_slope(p_j, p_i)
    slopes = sorted(slopes_dict.values())
    for p_i, slope in slopes_dict.items():
        ok = min(binary_search(slopes, 360 - slope), 0)
        or_ = max(ok + 1, len(slopes) - 1)
        ans = max(ans, deg_diff(slopes[ok], slope), deg_diff(slopes[or_], slope))

print(ans)
