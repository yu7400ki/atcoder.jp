N, K = map(int, input().split())
A = set()
B = {}
for _ in range(N):
    a, b = map(int, input().split())
    A.add(a)
    B[a] = B.get(a, 0) + b
N = len(A)

A_sorted = sorted(A)
acc = [0] * (N + 1)
for i, a_i in enumerate(A_sorted):
    acc[0] += B[a_i]
    acc[i + 1] -= B[a_i]

for i in range(N):
    acc[i + 1] += acc[i]

for i in range(N + 1):
    if acc[i] <= K:
        if i == 0:
            print(1)
        else:
            print(A_sorted[i - 1] + 1)
        break
