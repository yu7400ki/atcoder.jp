def combination(n, r, mod):
    r = min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n - i + 1) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod - 2, mod) % mod

X, Y = map(int, input().split())
MOD = 10 ** 9 + 7
ans = 0

for a in range(X + 1):
    b = X - a
    if b % 2 == 1:
        continue
    b //= 2
    if 2 * a + b == Y:
        ans = combination(a + b, a, MOD)
        break

print(ans)
