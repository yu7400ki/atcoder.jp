def combination(n, r, mod):
    r = min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n - i + 1) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod - 2, mod) % mod

N, A, B = map(int, input().split())

MOD = 10 ** 9 + 7

ans = pow(2, N, MOD) - 1
ans -= combination(N, A, MOD)
ans -= combination(N, B, MOD)

print(ans % MOD)
