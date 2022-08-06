cards = list(map(int,input().split()))

from collections import Counter

c = Counter(cards)
if len(c) == 2:
    for i in c:
        if c[i] == 2 or c[i] == 3:
            print('Yes')
            exit()
print('No')