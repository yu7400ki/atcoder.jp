N, P, Q, R = map(int,input().split())
A = list(map(int,input().split()))

def accumulate(l):
    res = [0] * (len(l) + 1)
    for i, n in enumerate(l):
        res[i+1] = res[i] + n
    return res

A_accum = accumulate(A)

def binary_search(ok,ng,func):
    while abs(ng - ok) > 1:
        mid = (ok+ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok

for x in range(N):
    y = binary_search(x, N+1, lambda m: A_accum[m] - A_accum[x] <= P)
    if A_accum[y] - A_accum[x] == P:
        z = binary_search(y, N+1, lambda m: A_accum[m] - A_accum[y] <= Q)
        if A_accum[z] - A_accum[y] == Q:
            w = binary_search(z, N+1, lambda m: A_accum[m] - A_accum[z] <= R)
            if A_accum[w] - A_accum[z] == R:
                print('Yes')
                exit()

print('No')