from collections import Counter
from itertools import combinations

def count_substrings(s):
    n = len(s)
    cnt = 0
    c = [Counter() for _ in range(n+1)]
    for i in range(1, n+1):
        c[i] = c[i-1] + Counter(s[i-1])
        for j in range(i):
            if all(x % 2 == 0 for x in (c[i] - c[j]).values()):
                cnt += 1
    return cnt

s = input()
print(count_substrings(s))