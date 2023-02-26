from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(set)
indegree = defaultdict(int)
history = set()

for _ in range(M):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph[X].add(Y)
    if (X, Y) in history:
        continue
    indegree[Y] += 1
    if X not in indegree:
        indegree[X] = 0
    history.add((X, Y))

res = [0] * N
i = 1
stack = []

for k, v in indegree.items():
    if v == 0:
        stack.append(k)

if len(stack) == 0 or len(stack) > 1:
    print("No")
    exit()

while stack:
    v = stack.pop()
    res[v] = i
    i += 1
    for w in graph[v]:
        indegree[w] -= 1
        if indegree[w] == 0:
            stack.append(w)
    if len(stack) > 1:
        print("No")
        exit()

if 0 in res:
    print("No")
else:
    print("Yes")
    print(" ".join(map(str, res)))
