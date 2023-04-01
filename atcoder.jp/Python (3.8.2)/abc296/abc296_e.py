from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

graph = defaultdict(int)

for i, a in enumerate(A):
    graph[i + 1] = a

A = set(i + 1 for i in range(N))

lose = set()
win = set()

while A:
    tmp = set()
    first = node = A.pop()
    tmp.add(node)

    while node not in graph or  graph[node] not in tmp:
        node = graph[node]
        tmp.add(node)
        A.discard(node)

    while tmp:
        if first != graph[node]:
            lose.add(first)
            tmp.discard(first)
            _first = graph[first]
            graph.pop(first)
            first = _first
        else:
            while tmp:
                pop = tmp.pop()
                win.add(pop)
                graph.pop(pop)

print(len(win))
