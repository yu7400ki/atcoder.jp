N, Q = map(int, input().split())
X = list(map(int, input().split()))

acc = [0] * (Q + 1)
s = set()
ans = [0] * N
idx = [0] * N

for i in range(Q):
    x = X[i] - 1
    if x in s:
        s.remove(x)
        ans[x] += acc[i] - acc[idx[x]]
    else:
        s.add(x)
        idx[x] = i
    acc[i + 1] += acc[i] + len(s)

for t in s:
    ans[t] += acc[Q] - acc[idx[t]]

print(*ans)
