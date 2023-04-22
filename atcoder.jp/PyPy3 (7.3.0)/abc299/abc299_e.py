from collections import defaultdict, deque

def bfs(graph, n, d):
    depth = defaultdict(lambda : -1)
    depth[n] = 0

    if d == 0:
        return depth

    queue = deque()
    queue.append(n)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                if depth[v] != d:
                    queue.append(v)

    return depth

N, M = map(int, input().split())

graph = defaultdict(set)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

K = int(input())

if K == 0:
    print("Yes")
    print("".join(["1"] * N))
    exit()

depths = {}
can_paint = set()
not_paint = set()
for _ in range(K):
    p, d = map(int, input().split())
    depth = bfs(graph, p, d)
    depths[p] = depth
    for node, dep in depth.items():
        if dep == d:
            can_paint.add(node)
        else:
            not_paint.add(node)

can_paint = can_paint - not_paint
if not can_paint:
    print("No")
    exit()

for depth in depths.values():
    flag = False
    for node in can_paint:
        if node in depth:
            flag = True
            break
    if not flag:
        print("No")
        exit()

ans = ["0"] * N
for node in can_paint:
    ans[node - 1] = "1"

print("Yes")
print("".join(ans))
