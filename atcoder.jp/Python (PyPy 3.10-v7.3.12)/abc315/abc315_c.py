from collections import defaultdict

FS = defaultdict(list)
N = int(input())
for _ in range(N):
    F, S = map(int, input().split())
    FS[F].append(S)
for f in FS.keys():
    FS[f].sort(reverse=True)

ma = []
for s in FS.values():
    ma.append(s[0])
ma.sort(reverse=True)

ans = -1
if len(ma) >= 2:
    ans = ma[0] + ma[1]

for s in FS.values():
    if len(s) >= 2:
        ans = max(ans, s[0] + s[1] // 2)

print(ans)
