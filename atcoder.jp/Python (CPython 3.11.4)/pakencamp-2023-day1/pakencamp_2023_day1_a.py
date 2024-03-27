from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)

if any(v <= 10 for v in cnt.values()):
    print("Yes")
else:
    print("No")
