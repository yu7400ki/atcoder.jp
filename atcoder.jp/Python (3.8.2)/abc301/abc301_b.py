N = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(N - 1):
    ans.append(A[i])
    if A[i] < A[i + 1]:
        for j in range(A[i + 1] - A[i] - 1):
            ans.append(A[i] + j + 1)
    elif A[i] > A[i + 1]:
        for j in range(A[i] - A[i + 1] - 1):
            ans.append(A[i] - j - 1)
ans.append(A[-1])

print(*ans)
