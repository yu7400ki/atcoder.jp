from math import ceil, floor

def sqrt(x):
    return x ** 0.5

def cbrt(x):
    return x ** (1 / 3)

def power(x, n):
    return x ** n

A, B = map(int, input().split())

def f(g):
    return A / sqrt(g) + (g - 1) * B

g = cbrt(power(A, 2) / (4 * power(B, 2)))

if g < 1:
    print(f(1))
else:
    print(min(f(floor(g)), f(ceil(g))))
