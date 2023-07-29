from bisect import bisect_right, bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ng = 0
ok = 10 ** 9 + 1

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    num_a = bisect_right(A, mid)
    idx = bisect_left(B, mid)
    num_b = M - idx
    if num_a >= num_b:
        ok = mid
    else:
        ng = mid

print(ok)
