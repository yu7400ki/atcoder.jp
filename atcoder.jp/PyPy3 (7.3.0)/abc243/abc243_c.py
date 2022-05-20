from collections import defaultdict

N = int(input())
XY = [tuple(map(int,input().split())) for _ in range(N)]
S = input()

L_max = defaultdict(lambda: -float('INF'))
R_min = defaultdict(lambda: float('INF'))

for s,(x,y) in zip(S,XY):
    if s == 'L':
        L_max[y] = max(L_max[y], x)
    else:
        R_min[y] = min(R_min[y], y)

for y in L_max:
    if R_min[y] < L_max[y]:
        print('Yes')
        break
else:
    print('No')