N = int(input())
A = [0] + list(map(int,input().split())) + [0]
Q = int(input())

A.sort()

for i in range(Q):
    B = int(input())
    
    ok = len(A) - 1
    ng = -1
    while ok - ng > 1:
        mid = (ok+ng) // 2
        if A[mid] > B:
            ok = mid
        else:
            ng = mid
    if ok == 0:
        ans = abs(A[1] - B)
        print(ans)
        continue
    elif ok == len(A):
        ok -= 1
    if ok > 1:
        if abs(A[ok] - B) > abs(A[ok-1] - B):
            ans = abs(A[ok-1] - B)
        else:
            ans = abs(A[ok] - B)
    else:
        ans = abs(A[ok] - B)

    print(ans)