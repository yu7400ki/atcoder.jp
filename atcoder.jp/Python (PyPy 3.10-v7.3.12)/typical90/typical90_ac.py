from atcoder.lazysegtree import LazySegTree

def op(x, y):
    return max(x, y)
def mapping(f, x):
    if f == -1:
        return x
    return f
def composition(f, g):
    if f == -1:
        return g
    return f
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
