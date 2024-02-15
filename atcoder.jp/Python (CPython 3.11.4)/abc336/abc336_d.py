N = int(input())
A = list(map(int, input().split()))

for _ in range(2):
    level = 0
    for i in range(N):
        if A[i] > level:
            level += 1
            A[i] = level
    A.reverse()

print(max(A))
