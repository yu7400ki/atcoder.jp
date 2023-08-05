N = int(input())
A = list(map(int, input().split()))

A.sort()
sum_a = sum(A)
b = [sum_a // N + (sum_a % N > i) for i in range(N)][::-1]
c = [abs(b[i] - A[i]) for i in range(N)]

print(sum(c) // 2)
