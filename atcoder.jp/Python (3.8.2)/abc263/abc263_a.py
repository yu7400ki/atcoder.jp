cards = list(map(int,input().split()))

from collections import Counter

print('Yes' if len(Counter(cards)) == 2 else 'No')