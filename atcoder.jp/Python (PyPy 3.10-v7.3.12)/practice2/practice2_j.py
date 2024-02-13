from atcoder.segtree import SegTree

inf = 1 << 60
op = lambda x, y: max(x, y)
e = -inf

N, Q = map(int, input().split())
A = list(map(int, input().split()))

st = SegTree(op, e, A)

for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        st.set(x - 1, y)
    elif t == 2:
        print(st.prod(x - 1, y))
    else:
        print(st.max_right(x - 1, lambda z: z < y) + 1)
