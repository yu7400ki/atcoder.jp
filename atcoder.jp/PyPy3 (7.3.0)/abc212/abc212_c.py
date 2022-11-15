N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()

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

ans = 1 << 62
for a in A:
    ok = binary_search(B, a)
    if ok == -1:
        ans = min(ans, abs(a - B[0]))
    elif ok == M - 1:
        ans = min(ans, abs(a - B[-1]))
    else:
        ans = min(ans, abs(a - B[ok]), abs(a - B[ok + 1]))

print(ans)
