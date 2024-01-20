N = int(input())
A = list(map(int, input().split()))
A = {a: i for i, a in enumerate(A)}

i = A[-1]
print(i + 1)
for _ in range(N - 1):
    i = A[i + 1]
    print(i + 1)
