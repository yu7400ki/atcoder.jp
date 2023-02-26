from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(set)
indegree = defaultdict(int)

for _ in range(M):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph[X].add(Y)

def topological_sort(graph, res):
    indegree = defaultdict(int)
    for k, v in graph.items():
        for w in v:
            indegree[w] += 1
        if k not in indegree:
            indegree[k] = 0
    stack = []
    for k, v in indegree.items():
        if v == 0:
            stack.append(k)
    if not stack or len(stack) > 1:
        return False
    while stack:
        v = stack.pop()
        res.append(v)
        for w in graph[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                stack.append(w)
        if len(stack) > 1:
            return False
    return True

res = []
is_ok = topological_sort(graph, res)
if not is_ok:
    print("No")
elif len(res) != N:
    print("No")
else:
    ans = [0] * N
    for i, v in enumerate(res):
        ans[v] = i + 1
    print("Yes")
    print(" ".join(map(str, ans)))
