N, Q = map(int, input().split())

graph = [set() for _ in range(N)]
not_isolate = set(range(N))

for _ in range(Q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        _, u, v = query
        u -= 1
        v -= 1
        graph[u].add(v)
        graph[v].add(u)
        not_isolate.discard(u)
        not_isolate.discard(v)
    elif query[0] == 2:
        _, v = query
        v -= 1
        for u in graph[v]:
            graph[u].remove(v)
            if len(graph[u]) == 0:
                not_isolate.add(u)
        not_isolate.add(v)
        graph[v] = set()
    print(len(not_isolate))
