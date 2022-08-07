N, K = map(int,input().split())

from math import gcd

if K == 1:
    print(0)
else:
    print(gcd(N, K))