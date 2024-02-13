from typing import NamedTuple
from atcoder.lazysegtree import LazySegTree


class S(NamedTuple):
    zero: int
    one: int
    inv: int

    def __add__(self, other):
        return S(
            self.zero + other.zero,
            self.one + other.one,
            self.inv + other.inv + self.one * other.zero,
        )

    def mapping(self, f):
        if f:
            return S(self.one, self.zero, self.zero * self.one - self.inv)
        return self

op = lambda x, y: x + y
mapping = lambda f, x: x.mapping(f)
composition = lambda f, g: g ^ f
e = S(0, 0, 0)
id_ = False

N, Q = map(int, input().split())
A = [S(1, 0, 0) if c == "0" else S(0, 1, 0) for c in input().split()]

seg = LazySegTree(op, e, mapping, composition, id_, A)

for _ in range(Q):
    t, l, r = map(int, input().split())
    if t == 1:
        seg.apply(l - 1, r, True)
    else:
        print(seg.prod(l - 1, r).inv)
