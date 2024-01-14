N = int(input())
A = list(map(int, input().split()))

A[0] = A[-1] = 1
for _ in range(2):
    for i in range(1, N):
        if A[i - 1] + 1 < A[i]:
            A[i] = A[i - 1] + 1
    A.reverse()

print(max(A))
