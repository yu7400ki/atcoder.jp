N, M = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))

color_idx = [[] for _ in range(M)]
for i, c in enumerate(C):
    color_idx[c-1].append(i)

change = {}
for idx in color_idx:
    if len(idx) <= 1:
        continue
    for i in range(len(idx)):
        change[idx[(i+1)%len(idx)]] = idx[i]

ans = S.copy()
for i, s in enumerate(S):
    if i in change:
        ans[i] = S[change[i]]

print("".join(ans))
