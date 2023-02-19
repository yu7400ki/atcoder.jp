N, K = map(int, input().split())
A = set(map(int, input().split()))

A = sorted(A)
if A[0] != 0:
    print(0)
    exit()

i = 0
while A[i] + 1 == A[i + 1]:
    i += 1

print(i)
