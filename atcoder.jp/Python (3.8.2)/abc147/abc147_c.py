from itertools import product

N = int(input())

HONEST = 1
UNKIND = 0

t = [[] for _ in range(N)]
for i in range(N):
    A = int(input())
    for _ in range(A):
        x, y = map(int, input().split())
        t[i].append((x-1, y))

ans = 0
for bits in product([HONEST, UNKIND], repeat=N):
    flag = True
    for i, bit in enumerate(bits):
        if bit == UNKIND:
            continue
        for x, y in t[i]:
            if bits[x] != y:
                flag = False
                break
    if flag:
        ans = max(ans, sum(bits))

print(ans)
