N, M = map(int, input().split())

pairs = {(i, j): False for i in range(N) for j in range(N)}

for _ in range(M):
    k, *x = map(int, input().split())
    for i in range(k):
        for j in range(k):
            pairs[(x[i] - 1, x[j] - 1)] = True
            pairs[(x[j] - 1, x[i] - 1)] = True

if all(pairs.values()):
    print("Yes")
else:
    print("No")
