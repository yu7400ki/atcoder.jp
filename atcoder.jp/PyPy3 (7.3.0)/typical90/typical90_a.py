N, L = map(int,input().split())
K = int(input())
A = [0] + list(map(int,input().split())) + [L]

def can_cut(n):
    cnt = 0
    l = 0
    for i in range(1,N+2):
        l += A[i] - A[i-1]
        if l >= n:
            cnt += 1
            l = 0
    return cnt >= K+1

ok = -1
ng = L
while ng - ok > 1:
    mid = (ok+ng) // 2
    if can_cut(mid):
        ok = mid
    else:
        ng = mid

print(ok)