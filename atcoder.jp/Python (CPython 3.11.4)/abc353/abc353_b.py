N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 1
k = K
while A:
    if A[0] <= k:
        k -= A.pop(0)
    else:
        ans += 1
        k = K

print(ans)
