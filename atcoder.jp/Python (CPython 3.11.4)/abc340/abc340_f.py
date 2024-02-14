from math import gcd

def ext_gcd(a, b):
    if b == 0:
        return 1, 0
    else:
        y, x = ext_gcd(b, a % b)
        y -= a // b * x
        return x, y

X, Y = map(int, input().split())

g = gcd(X, Y)
if g >= 3:
    print(-1)
else:
    x, y = ext_gcd(X, -Y)
    print(2 // g * x, 2 // g * y)
