from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(set)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

start = 0
end = N + 1
for i in range(1, N + 1):
    if len(graph[i]) == 1:
        if start == 0:
            start = i
        elif end == N + 1:
            end = i
        else:
            print("No")
            exit()

if start == 0 or end == N + 1:
    print("No")
    exit()

pos = start
visited = set([pos])
while pos != end:
    for next in graph[pos]:
        visited.add(next)
        if len(graph[next]) == 2:
            graph[next].remove(pos)
            pos = next
            break
        if len(graph[next]) == 1:
            if next == end:
                pos = next
                break
    else:
        print("No")
        exit()

if len(visited) == N:
    print("Yes")
else:
    print("No")
