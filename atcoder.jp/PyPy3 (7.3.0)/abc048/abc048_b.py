A, B, X = map(int, input().split())

mi = (A + X - 1) // X * X
ma = B // X * X

if mi > ma:
    print(0)
elif mi == ma:
    print(1)
else:
    print(2 + (ma - mi - 1) // X)
