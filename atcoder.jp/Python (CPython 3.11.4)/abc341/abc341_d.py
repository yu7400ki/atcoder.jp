from math import lcm

N, M, K = map(int, input().split())
l = lcm(N, M)

ok = 10 ** 18
ng = 0

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    cnt = mid // N + mid // M - mid // l * 2
    if cnt >= K:
        ok = mid
    else:
        ng = mid

print(ok)
