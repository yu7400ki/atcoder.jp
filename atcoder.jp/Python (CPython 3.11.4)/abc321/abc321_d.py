N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()

acc = [0] * (M + 1)
for i in range(M):
    acc[i + 1] = acc[i] + B[i]


def binary_search(x):
    ok = -1
    ng = M
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if B[mid] <= x:
            ok = mid
        else:
            ng = mid
    return ok


ans = 0
for a in A:
    d = P - a
    if d < 0:
        ret = P * M
    else:
        idx = binary_search(d)
        if idx == -1:
            ret = P * M
        else:
            rest = M - idx - 1
            ret = a * (idx + 1) + acc[idx + 1] + rest * P
    ans += ret

print(ans)
