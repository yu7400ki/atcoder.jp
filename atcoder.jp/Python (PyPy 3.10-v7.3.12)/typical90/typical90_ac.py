from atcoder.lazysegtree import LazySegTree

op = max
mapping = lambda f, x: f if f != -1 else x
composition = lambda f, g: f if f != -1 else g
e = -1
_id = -1

W, N = map(int, input().split())

seg = LazySegTree(op, e, mapping, composition, _id, [0] * W)

for _ in range(N):
    L, R = map(int, input().split())
    L -= 1
    v = seg.prod(L, R)
    seg.apply(L, R, v + 1)
    print(v + 1)
