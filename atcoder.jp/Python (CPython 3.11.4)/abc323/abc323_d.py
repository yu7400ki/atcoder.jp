def count_one(n):
    c = 0
    while n > 0:
        if n & 1:
            c += 1
        n >>= 1
    return c

from collections import defaultdict

N = int(input())
slime = defaultdict(int)
for _ in range(N):
    s, c = map(int, input().split())
    slime[s] = c

new_slime = defaultdict(int)
for s, c in slime.items():
    i = 0
    while s & 1 == 0:
        s >>= 1
        i += 1
    new_slime[s] += c * (2 ** i)

ans = 0
for c in new_slime.values():
    ans += count_one(c)

print(ans)
