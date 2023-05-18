N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def is_ok(x):
    cnt = 0
    pre = 0
    for a in A:
        if a - pre >= x:
            cnt += 1
            pre = a
    if L - pre >= x:
        cnt += 1
    return cnt >= K + 1


def binary_search(ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(binary_search(0, L + 1))
