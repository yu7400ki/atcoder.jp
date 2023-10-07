from collections import defaultdict

N = int(input())
slime = defaultdict(int)
for _ in range(N):
    s, c = map(int, input().split())
    slime[s] = c

new_slime = defaultdict(int)
for s, c in slime:
    i = 0
    while s & 1 == 0:
        s >>= 1
        i += 1
    new_slime[s] += c * (2 ** i)

ans = 0
for c in new_slime.values():
    ans += c.bit_count()

print(ans)
