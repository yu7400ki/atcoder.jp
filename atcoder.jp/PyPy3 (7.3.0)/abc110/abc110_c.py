from collections import defaultdict

S = list(input())
T = list(input())

graph = defaultdict(set)
for i in range(len(S)):
    graph[T[i]].add(S[i])

if all(len(v) == 1 for v in graph.values()):
    print("Yes")
else:
    print("No")
