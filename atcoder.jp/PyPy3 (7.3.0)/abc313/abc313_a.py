from collections import Counter

N = int(input())
P = list(map(int, input().split()))

ma = max(P)
count = Counter(P)

if P[0] != ma:
    print(ma - P[0] + 1)
else:
    if count[ma] == 1:
        print(0)
    else:
        print(1)
