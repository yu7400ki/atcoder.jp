from atcoder.segtree import SegTree

inf = 1 << 60
op = lambda x, y: max(x, y)
e = -inf

N, Q = map(int, input().split())

st = SegTree(op, e, [0] * N)

for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        st.set(x - 1, y)
    else:
        print(st.prod(x - 1, y - 1))
