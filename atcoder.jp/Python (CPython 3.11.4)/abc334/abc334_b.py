A, M, L, R = map(int, input().split())

L -= A
R -= A

l = L + (M - L % M) % M
r = R - R % M

if r < l:
    print(0)
else:
    print((r - l) // M + 1)
