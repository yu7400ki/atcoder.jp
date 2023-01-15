import networkx as nx

N = int(input())

graph = nx.DiGraph()
for _ in range(N):
    S, T = input().split()
    graph.add_edge(S, T)

if nx.is_directed_acyclic_graph(graph):
    print("Yes")
else:
    print("No")
