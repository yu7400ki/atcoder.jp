N = int(input())
A = list(map(int, input().split()))

sleep_time = {0: 0}
last = 0
for i in range(2, N, 2):
    sleep_time[A[i]] = A[i] - A[i - 1] + sleep_time[last]
    last = A[i]

A_odd = A[::2]
A_even = [0] + A[1::2]

def binary_search(lst, target):
    ng = -1
    ok = len(lst)
    key = (lambda x: lst[x] >= target)

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if key(mid):
            ok = mid
        else:
            ng = mid

    return ok

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    l_wake = A_odd[binary_search(A_odd, l)]
    l_sleep_idx = min(binary_search(A_even, l), len(A_even) - 1)
    if A_even[l_sleep_idx] > l_wake:
        l_sleep_idx -= 1
    l_sleep = A_even[l_sleep_idx]
    r_wake = A_odd[binary_search(A_odd, r)]
    r_sleep_idx = min(binary_search(A_even, r), len(A_even) - 1)
    if A_even[r_sleep_idx] > r_wake:
        r_sleep_idx -= 1
    r_sleep = A_even[r_sleep_idx]
    time = sleep_time[r_wake] - sleep_time[l_wake]
    time -= r_wake - max(r, r_sleep)
    time += l_wake - max(l, l_sleep)
    print(time)
