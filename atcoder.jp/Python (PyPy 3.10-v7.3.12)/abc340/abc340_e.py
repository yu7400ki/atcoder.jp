from atcoder.lazysegtree import LazySegTree as _LazySegTree

class LazySegTree(_LazySegTree):
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __len__(self):
        return self._n

    def __str__(self):
        return str([self[i] for i in range(len(self))])

    def __iter__(self):
        return (self[i] for i in range(len(self)))

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

op = lambda a, b: 0
e = 0
mapping = lambda f, x: x + f
composition = lambda f, g: g + f
id_ = 0

seg = LazySegTree(op, e, mapping, composition, id_, A)
for b in B:
    x = seg[b]
    seg[b] = 0
    d, r = x // N, x % N
    seg.apply(0, N, d)
    b += 1
    if b + r < N:
        seg.apply(b, b + r, 1)
    else:
        seg.apply(b, N, 1)
        seg.apply(0, (b + r) % N, 1)

print(*seg)
