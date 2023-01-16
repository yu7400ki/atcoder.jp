from collections import defaultdict, deque

N = int(input())

graph = defaultdict(set)

for _ in range(N):
    S, T = input().split()
    graph[S].add(T)

def hasCycle(graph):
    nodes = set(graph.keys())

    def bfs(graph, n):
        depth = defaultdict(lambda : -1)
        depth[n] = 0
        queue = deque()
        queue.append(n)

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if depth[v] == -1:
                    queue.append(v)
                    depth[v] = depth[u] + 1
                else:
                    return True

        return depth

    while nodes:
        n = nodes.pop()
        depth = bfs(graph, n)
        if depth == True:
            return True
        nodes -= set(depth.keys())

    return False

if not hasCycle(graph):
    print("Yes")
else:
    print("No")
