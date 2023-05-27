from collections import defaultdict

N = int(input())
graph = defaultdict(set)
degree = defaultdict(int)
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
    degree[u] += 1
    degree[v] += 1

degree_one = set()
for e, d in degree.items():
    if d == 1:
        degree_one.add(e)

levels = []
while degree_one:
    e = degree_one.pop()
    r = graph[e].pop()
    levels.append(len(graph[r]))
    for e in graph[r]:
        for f in graph[e]:
            if f == r:
                continue
            degree[f] -= 1
            graph[f].discard(e)
            if degree[f] == 1:
                degree_one.add(f)
        del graph[e]
        degree_one.discard(e)
    del graph[r]

levels.sort()
print(" ".join(map(str, levels)))
