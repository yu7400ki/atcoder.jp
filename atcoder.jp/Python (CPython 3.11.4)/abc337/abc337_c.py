N = int(input())
A = list(map(int, input().split()))
A = {a: i for i, a in enumerate(A)}

a = A[-1] + 1
print(a)
for _ in range(N - 1):
    a = A[a] + 1
    print(a)
