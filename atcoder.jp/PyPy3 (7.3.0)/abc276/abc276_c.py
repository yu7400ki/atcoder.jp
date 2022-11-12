N = int(input())
P = list(map(int,input().split()))

idx1 = N - 1
while P[idx1] > P[idx1 - 1]:
    idx1 -= 1
idx1 -= 1

idx2 = P.index(P[idx1] - 1)

P[idx1], P[idx2] = P[idx2], P[idx1]

print(*P[:idx1 + 1], *sorted(P[idx1 + 1:], reverse=True))
