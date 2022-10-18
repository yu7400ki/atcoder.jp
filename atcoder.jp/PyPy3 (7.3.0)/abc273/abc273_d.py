from collections import defaultdict

H, W, rs, cs = map(int, input().split())
N = int(input())

walls_x = defaultdict(list)
walls_y = defaultdict(list)

for _ in range(N):
    r, c = map(int, input().split())
    walls_x[r].append(c)
    walls_y[c].append(r)

for _, v in walls_x.items():
    v.append(0)
    v.append(W + 1)
    v.sort()

for _, v in walls_y.items():
    v.append(0)
    v.append(H + 1)
    v.sort()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def binary_search(lst, target = None, ok = -1, ng = None, key = None):
    ng = len(lst) if ng is None else ng
    key = (lambda x: lst[x] <= target) if key is None else key

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if key(mid):
            ok = mid
        else:
            ng = mid

    return ok

pos = Point(cs, rs)

Q = int(input())

for _ in range(Q):
    d, l = input().split()
    l = int(l)

    if d == "L":
        if pos.y in walls_x:
            p = binary_search(walls_x[pos.y], key=lambda m: walls_x[pos.y][m] < pos.x)
            pos.x = max(walls_x[pos.y][p] + 1, pos.x - l)
        else:
            pos.x = max(1, pos.x - l)
    elif d == "R":
        if pos.y in walls_x:
            p = binary_search(walls_x[pos.y], key=lambda m: walls_x[pos.y][m] > pos.x, ok=len(walls_x[pos.y])-1, ng=-1)
            pos.x = min(walls_x[pos.y][p] - 1, pos.x + l)
        else:
            pos.x = min(W, pos.x + l)
    elif d == "U":
        if pos.x in walls_y:
            p = binary_search(walls_y[pos.x], key=lambda m: walls_y[pos.x][m] < pos.y)
            pos.y = max(walls_y[pos.x][p] + 1, pos.y - l)
        else:
            pos.y = max(1, pos.y - l)
    elif d == "D":
        if pos.x in walls_y:
            p = binary_search(walls_y[pos.x], key=lambda m: walls_y[pos.x][m] > pos.y, ok=len(walls_y[pos.x])-1, ng=-1)
            pos.y = min(walls_y[pos.x][p] - 1, pos.y + l)
        else:
            pos.y = min(H, pos.y + l)

    print(pos.y, pos.x)
