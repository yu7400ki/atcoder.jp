N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

A_accum = [0] * (N + 1)
for i, n in enumerate(A):
    A_accum[i + 1] = A_accum[i] + n

def binary_search(lst, key, ok = -1, ng = None, f = None):
    ng = len(lst) if ng is None else ng
    f = (lambda x: lst[x] <= key) if f is None else f
    
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    
    return ok

for _ in range(Q):
    X = int(input())
    ok = binary_search(A, X)
    if ok == -1:
        ans = A_accum[-1] - X * N
    else:
        ans = (X * (ok + 1) - A_accum[ok + 1]) + (A_accum[N] - A_accum[ok + 1] - (N - ok - 1) * X)
    print(ans)
