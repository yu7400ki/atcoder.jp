from collections import Counter

s = list(input())
c = Counter(s)

for k, v in c.items():
    if v == 1:
        print(s.index(k) + 1)
        break
