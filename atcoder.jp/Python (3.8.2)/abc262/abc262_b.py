from collections import defaultdict
N, M = map(int,input().split())

graph = defaultdict(set)
for _ in range(M):
    U, V = map(int,input().split())
    graph[U].add(V)
    graph[V].add(U)

ans = 0
for a in range(1, N+1):
    for b in range(a+1, N+1):
        for c in range(b+1, N+1):
            if b in graph[a] and c in graph[b] and a in graph[c]:
                ans += 1

print(ans)