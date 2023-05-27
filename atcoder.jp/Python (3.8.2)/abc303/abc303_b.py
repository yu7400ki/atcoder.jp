N, M = map(int, input().split())

pairs = set()
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        pairs.add((i, j))

for _ in range(M):
    A = list(map(int, input().split()))
    for i in range(N - 1):
        pairs.discard((A[i], A[i + 1]))
        pairs.discard((A[i + 1], A[i]))

print(len(pairs))
