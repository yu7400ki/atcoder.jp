N, Q = map(int, input().split())

l = [(i + 1, 0) for i in range(N)]
l.reverse()

d = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
for _ in range(Q):
    t, c = input().split()
    if t == "1":
        dx, dy = d[c]
        nx, ny = l[-1][0] + dx, l[-1][1] + dy
        l.append((nx, ny))
    else:
        p = int(c)
        print(l[-p][0], l[-p][1])
