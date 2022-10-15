from collections import Counter

N = int(input())
A = list(map(int, input().split()))
count = Counter(A)

_A_idx = [(a, i) for i, a in enumerate(A)]
_A_idx.sort()
history = set()
A_idx = []
for a, i in _A_idx:
    if a in history:
        continue
    else:
        A_idx.append((a, i))
        history.add(a)

ans = {}
for i in range(len(A_idx)):
    ans[len(A_idx) - i - 1] = A_idx[i][0]

for i in range(N):
    if i in ans:
        print(count[ans[i]])
    else:
        print(0)