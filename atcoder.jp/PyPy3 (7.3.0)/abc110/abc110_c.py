from collections import defaultdict

S = list(input())
T = list(input())

graph1 = defaultdict(set)
graph2 = defaultdict(set)
for i in range(len(S)):
    graph1[T[i]].add(S[i])
    graph2[S[i]].add(T[i])

if all(len(v) <= 1 for v in graph1.values()) and all(len(v) <= 1 for v in graph2.values()):
    print("Yes")
else:
    print("No")
