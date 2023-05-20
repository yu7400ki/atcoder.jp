N, M, D = map(int, input().split())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

def binary_search(lst, target, ok = -1, ng = None, key = None):
    ng = len(lst) if ng is None else ng
    key = (lambda x: lst[x] <= target) if key is None else key

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if key(mid):
            ok = mid
        else:
            ng = mid

    return ok

ans = -1
for a in A:
    ok = binary_search(B, D + a)
    if ok >= 0:
        b = B[ok]
        if abs(a - b) <= D:
            ans = max(ans, a + b)

print(ans)
