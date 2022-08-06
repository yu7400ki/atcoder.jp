from itertools import combinations

N, M = map(int, input().split())

for el in combinations(range(1, M+1), N):
    print(' '.join(map(str, el)))