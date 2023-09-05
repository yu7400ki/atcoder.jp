from collections import Counter

N = int(input())
A = list(map(int, input().split()))

count = Counter(A)
l = sorted(count.keys(), reverse=True)
d = {}
for i in range(len(l)):
    d[i] = l[i]

for k in range(N):
    print(count.get(d.get(k, -1), 0))
