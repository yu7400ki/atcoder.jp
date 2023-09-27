N, K = map(int, input().split())
a = list(map(int, input().split()))

l = [[] for _ in range(K)]

for k in range(K):
    for i in range(k, N, K):
        l[k].append(a[i])
for li in l:
    li.sort()

ans = [0] * N
for k in range(K):
    for i in range(len(l[k])):
        ans[k + i * K] = l[k][i]

if sorted(ans) == ans:
    print("Yes")
else:
    print("No")
