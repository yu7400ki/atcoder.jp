Q = int(input())

q = []
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        q.insert(0, x)
    elif t == 2:
        print(q[x - 1])
