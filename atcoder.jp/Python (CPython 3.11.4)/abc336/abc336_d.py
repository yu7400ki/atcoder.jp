N = int(input())
A = [0] + list(map(int, input().split())) + [0]

for _ in range(2):
    for i in range(N + 2):
        A[i] = min(A[i], A[i - 1] + 1, i)
    A.reverse()

print(max(A))
