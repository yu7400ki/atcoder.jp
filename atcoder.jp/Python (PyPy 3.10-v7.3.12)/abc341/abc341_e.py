from atcoder.segtree import SegTree

N, Q = map(int, input().split())
S = list(input())
S = [0] + [1 if S[i] == S[i + 1] else 0 for i in range(N - 1)] + [0]

op = max
e = 0

seg = SegTree(op, e, S)

for _ in range(Q):
    t, l, r = map(int, input().split())
    if t == 1:
        seg.set(l - 1, 1 - seg.get(l - 1))
        seg.set(r, 1 - seg.get(r))
    else:
        print("No" if seg.prod(l, r) else "Yes")
