N, M, X = map(int,input().split())
A = list(map(int,input().split()))

cost1 = 0
cost2 = 0

for i in range(X, N+1):
    if i in A:
        cost1 += 1

for i in range(X, -1, -1):
    if i in A:
        cost2 += 1

print(min(cost1, cost2))