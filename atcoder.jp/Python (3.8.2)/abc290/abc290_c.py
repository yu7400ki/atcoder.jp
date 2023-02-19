N, K = map(int, input().split())
A = set(map(int, input().split()))

A = sorted(A)

if len(A) < K or A[K - 1] != K - 1:
    print(0)
    exit()
else:
    print(K)
