from heapq import heappop, heappush

N, A, B, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(N)]

INF = 1 << 60
def dijkstra(s: int, f) -> list[int]:
    dist = [INF] * N
    dist[s] = 0
    queue = [(0, s)]
    while queue:
        d, v = heappop(queue)
        if d > dist[v]:
            continue
        for nv, nd in enumerate(D[v]):
            if dist[nv] > dist[v] + f(nd):
                dist[nv] = dist[v] + f(nd)
                heappush(queue, (dist[nv], nv))
    return dist

car = dijkstra(0, lambda x: x * A)
train = dijkstra(N - 1, lambda x: x * B + C)

ans = INF
for i in range(N):
    tmp = car[i] + train[i]
    ans = min(ans, tmp)

print(ans)
