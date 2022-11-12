N = int(input())
P = list(map(int,input().split()))

idx1 = N - 1
while P[idx1] > P[idx1 - 1]:
    idx1 -= 1
idx1 -= 1

idx2 = idx1
while idx2 < N-1 and P[idx2 + 1] < P[idx1]:
    idx2 += 1

P[idx1], P[idx2] = P[idx2], P[idx1]

print(*P[:idx1 + 1], *sorted(P[idx1 + 1:], reverse=True))
