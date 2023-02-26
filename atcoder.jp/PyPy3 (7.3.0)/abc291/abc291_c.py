from collections import namedtuple

N = int(input())
S = list(input())
Point = namedtuple('Point', ['x', 'y'])

pos = Point(0, 0)
history = set([pos])
ans = "No"

for s in S:
    if s == 'R':
        pos = Point(pos.x + 1, pos.y)
    elif s == 'L':
        pos = Point(pos.x - 1, pos.y)
    elif s == 'U':
        pos = Point(pos.x, pos.y + 1)
    elif s == 'D':
        pos = Point(pos.x, pos.y - 1)
    if pos in history:
        ans = "Yes"
        break
    history.add(pos)

print(ans)
