from more_itertools import powerset
from itertools import product

N, H, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]


def to_bit(a, b):
    if a > H and b > W:
        raise ValueError
    bit = 0
    for i in range(H):
        for j in range(W):
            if i < a and j < b:
                bit |= 1 << (i * H + j)
    return bit


ans = False
for p in powerset(AB):
    if sum(a * b for a, b in p) != H * W:
        continue
    for q in product(range(H), repeat=len(p)):
        for r in product(range(W), repeat=len(p)):
            for s in product(range(2), repeat=len(p)):
                bit = 0
                for (a, b), y, x, f in zip(p, q, r, s):
                    if f:
                        a, b = b, a
                    bit |= to_bit(a, b) << (y * H + x)
                if bit == (1 << (H * W)) - 1:
                    ans = True
                    break

if ans:
    print("Yes")
else:
    print("No")
