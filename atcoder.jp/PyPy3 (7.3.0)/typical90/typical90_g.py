N = int(input())
A = list(map(int,input().split()))
Q = int(input())

A.sort()

for i in range(Q):
    B = int(input())
    
    ok = len(A)
    ng = -1
    while ok - ng > 1:
        mid = (ok+ng) // 2
        if A[mid] > B:
            ok = mid
        else:
            ng = mid
    if ok == len(A):
        ok -= 1
    if ok >= 1:
        if abs(A[ok] - B) < abs(A[ok-1] - B):
            ans = abs(A[ok] - B)
        else:
            ans = abs(A[ok-1] - B)
    else:
        ans = abs(A[ok] - B)

    print(ans)