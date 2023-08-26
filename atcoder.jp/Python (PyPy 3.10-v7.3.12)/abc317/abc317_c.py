from collections import defaultdict
from itertools import permutations

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

ans = 0
for p in permutations(range(1, N + 1)):
    tmp = 0
    for i in range(N - 1):
        a, b = p[i], p[i + 1]
        for c, d in graph[a]:
            if c == b:
                tmp += d
                break
        else:
            break
    ans = max(ans, tmp)

print(ans)
