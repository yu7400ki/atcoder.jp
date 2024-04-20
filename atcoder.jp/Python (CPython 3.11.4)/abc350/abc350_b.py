N, Q = map(int, input().split())
T = list(map(int, input().split()))

l = [True] * N
for t in T:
    l[t - 1] = not l[t - 1]

ans = sum(l)
print(ans)
