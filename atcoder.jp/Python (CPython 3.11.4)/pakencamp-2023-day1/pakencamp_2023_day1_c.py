N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

if A[0] + A[1] > A[2]:
    print("Yes")
else:
    print("No")
