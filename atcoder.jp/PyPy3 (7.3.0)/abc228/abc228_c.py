N, K = map(int, input().split())
P = [sum(map(int, input().split())) for _ in range(N)]

sorted_P = sorted(P, reverse=True)

k = sorted_P[K-1]

for p in P:
    if p + 300 >= k:
        print("Yes")
    else:
        print("No")
