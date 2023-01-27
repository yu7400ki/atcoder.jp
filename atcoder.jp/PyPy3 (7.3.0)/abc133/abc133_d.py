N = int(input())
A = list(map(int, input().split()))

S = sum(A)
X = [0] * N
X[0] = S - 2 * sum(A[1::2])

for i in range(N - 1):
    X[i + 1] = 2 * A[i] - X[i]

print(*X)
