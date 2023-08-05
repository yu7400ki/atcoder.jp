N, M = map(int, input().split())

indegree = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    indegree[b - 1] += 1

if indegree.count(0) == 1:
    print(indegree.index(0) + 1)
else:
    print(-1)
