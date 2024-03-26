N = int(input())
A = list(map(int, input().split()))

for a, b in zip(A, A[1:]):
    print(a * b)
