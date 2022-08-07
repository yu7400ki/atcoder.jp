K, N = map(int,input().split())
A = list(map(int,input().split()))

ma = 0
for i in range(N):
    if i != N-1:
        if ma < A[i+1] - A[i]:
            ma = A[i+1] - A[i]
    else:
        if ma < K - A[i] + A[0]:
            ma = K - A[i] + A[0]

print(K - ma)