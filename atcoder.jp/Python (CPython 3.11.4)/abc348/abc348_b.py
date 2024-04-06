N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]


def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


for p in points:
    ans = points.index(max(points, key=lambda x: dist(p, x)))
    print(ans + 1)
