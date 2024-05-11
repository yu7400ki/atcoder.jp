from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
A.sort()
MOD = 10**8

cnt = 0
for i in range(N):
    idx = bisect_left(A, MOD - A[i], i + 1)
    cnt += N - idx

ans = sum(a * (N - 1) for a in A) - cnt * MOD
print(ans)
