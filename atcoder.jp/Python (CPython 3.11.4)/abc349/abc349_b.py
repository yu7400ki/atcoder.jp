from collections import Counter

S = list(input())

cnt = {}
for v in Counter(S).values():
    cnt[v] = cnt.get(v, 0) + 1

if all(v == 2 for v in cnt.values()):
    print("Yes")
else:
    print("No")
