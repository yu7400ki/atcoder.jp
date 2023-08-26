N, H, X = map(int, input().split())
P = list(map(int, input().split()))

d = X - H
for i, p in enumerate(P):
    if p >= d:
        print(i + 1)
        break
