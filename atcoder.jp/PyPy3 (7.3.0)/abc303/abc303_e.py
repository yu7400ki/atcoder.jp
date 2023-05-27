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

levels = []
while True:
    deletable = []
    for e, d in degree.items():
        if d != 1:
            continue
        r = graph[e].pop()
        levels.append(len(graph[r]))
        for e in graph[r]:
            for f in graph[e]:
                if f == r:
                    continue
                degree[f] -= 1
                graph[f].discard(e)
            degree[e] = 0
            del graph[e]
            deletable.append(e)
        degree[r] = 0
        del graph[r]
        deletable.append(r)
        break
    else:
        break
    for e in deletable:
        del degree[e]

levels.sort()
print(" ".join(map(str, levels)))
