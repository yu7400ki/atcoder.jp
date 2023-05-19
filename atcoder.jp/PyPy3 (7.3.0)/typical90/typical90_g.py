N = int(input())
A = sorted(map(int, input().split()))
Q = int(input())

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

for _ in range(Q):
    B = int(input())
    ok = max(binary_search(A, B), 0)
    or_ = min(ok + 1, N - 1)
    print(min(map(abs, [A[ok] - B, A[or_] - B])))
