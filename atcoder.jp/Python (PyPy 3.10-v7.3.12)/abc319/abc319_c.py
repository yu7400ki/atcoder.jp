from itertools import permutations

c = [list(map(int, input().split())) for _ in range(3)]

total = 362880
res = 0

for p in permutations(range(9)):
    vertical = [[], [], []]
    horizontal = [[], [], []]
    diag = [[], []]
    for i in p:
        x = i // 3
        y = i % 3
        vertical[x].append(c[x][y])
        horizontal[y].append(c[x][y])
        if x == y:
            diag[0].append(c[x][y])
        if x + y == 2:
            diag[1].append(c[x][y])
        flag = True
    for v in vertical:
        if v[0] == v[1] and v[0] != v[2]:
            flag = False
            break
    for h in horizontal:
        if h[0] == h[1] and h[0] != h[2]:
            flag = False
            break
    for d in diag:
        if d[0] == d[1] and d[0] != d[2]:
            flag = False
            break
    res += flag

print(res / total)
