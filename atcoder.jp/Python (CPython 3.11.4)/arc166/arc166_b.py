from itertools import permutations
from math import lcm

N, A, B, C = map(int, input().split())
Ai = list(map(int, input().split()))

inf = 1 << 60
ans = inf

if N >= 3:
    tmp = inf
    s = [A, B, C]
    for p in permutations(s):
        tmp2 = 0
        used = []
        for i in range(3):
            tmp3 = (inf, inf)
            for j, a in enumerate(Ai):
                if j in used:
                    continue
                tmp3 = min(tmp3, ((p[i] - a % p[i]) % p[i], j), key=lambda x: x[0])
            tmp2 += tmp3[0]
            used.append(tmp3[1])
        tmp = min(tmp, tmp2)
    ans = tmp

if N >= 2:
    sc = [[lcm(A, B), C], [lcm(A, C), B], [lcm(B, C), A]]
    for s in sc:
        tmp = inf
        for p in permutations(s):
            tmp2 = 0
            used = []
            for i in range(2):
                tmp3 = (inf, inf)
                for j, a in enumerate(Ai):
                    if j in used:
                        continue
                    tmp3 = min(tmp3, ((p[i] - a % p[i]) % p[i], j), key=lambda x: x[0])
                tmp2 += tmp3[0]
                used.append(tmp3[1])
            tmp = min(tmp, tmp2)
        ans = min(ans, tmp)

if N >= 1:
    pi = lcm(A, lcm(B, C))
    tmp = inf
    for a in Ai:
        tmp = min(tmp, (pi - a % pi) % pi)
    ans = min(ans, tmp)

print(ans)
