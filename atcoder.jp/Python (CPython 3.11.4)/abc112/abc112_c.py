from itertools import product

N = int(input())
xyh = [tuple(map(int, input().split())) for _ in range(N)]

for cx, cy in product(range(101), repeat=2):
    heights = []
    for x, y, h in xyh:
        if h == 0:
            continue
        H = h + abs(x - cx) + abs(y - cy)
        heights.append(H)
    if len(set(heights)) == 1:
        H = heights[0]
        for x, y, h in xyh:
            if h != max(H - abs(x - cx) - abs(y - cy), 0):
                break
        else:
            print(cx, cy, H)
            exit()
