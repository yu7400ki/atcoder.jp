import networkx as nx

G = nx.Graph()
N = int(input())
edges = []

for i in range(1, N):
    D = list(map(int, input().split()))
    for j, d in enumerate(D):
        edges.append((i, i + j + 1, d))

G.add_weighted_edges_from(edges)
matching = nx.max_weight_matching(G)

ans = 0
for u, v in matching:
    ans += G[u][v]["weight"]

print(ans)
