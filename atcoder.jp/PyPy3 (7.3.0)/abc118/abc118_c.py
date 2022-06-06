from math import gcd
from functools import reduce

N = int(input())
A = list(map(int,input().split()))

ans = reduce(gcd, A)
print(ans)