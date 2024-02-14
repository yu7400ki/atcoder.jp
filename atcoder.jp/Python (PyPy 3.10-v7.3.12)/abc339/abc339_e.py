from atcoder.segtree import SegTree

N, D = map(int, input().split())
A = list(map(int, input().split()))

op = max
e = 0
seg = SegTree(op, e, 10 ** 6)

for a in A:
    l = max(0, a - D)
    r = min(10 ** 6, a + D)
    v = seg.prod(l, r + 1)
    seg.set(a, v + 1)

print(seg.all_prod())
