from atcoder.lazysegtree import LazySegTree

H, W, M = map(int, input().split())
TAX = [list(map(int, input().split())) for _ in range(M)]
TAX.reverse()

mapping = lambda x, y: x + y
composition = lambda x, y: x + y
hc = LazySegTree(lambda x, y: 0, 0, mapping, composition, 0, [W] * H)
wc = LazySegTree(lambda x, y: 0, 0, mapping, composition, 0, [H] * W)

cnt = {-1: H * W}

for t, a, x in TAX:
    if t == 1:
        r = hc.get(a - 1)
        if r <= 0:
            continue
        hc.set(a - 1, 0)
        wc.apply(0, W, -1)
    else:
        r = wc.get(a - 1)
        if r <= 0:
            continue
        wc.set(a - 1, 0)
        hc.apply(0, H, -1)
    cnt[x] = cnt.get(x, 0) + r
    cnt[-1] -= r

cnt[0] = cnt.get(0, 0) + cnt[-1]
cnt[-1] = 0
ans = []
for k, v in sorted(cnt.items(), key=lambda x: x[0]):
    if v <= 0:
        continue
    ans.append((k, v))

print(len(ans))
for k, v in ans:
    print(k, v)
