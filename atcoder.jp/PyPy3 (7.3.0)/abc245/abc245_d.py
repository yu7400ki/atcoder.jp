N, M = map(int,input().split())
A = list(map(int,input().split()))[::-1]
C = list(map(int,input().split()))[::-1]

B = []
for i in range(M+1):
    b = C[i] // A[0]
    B.append(b)
    for j in range(N+1):
        C[j+i] -= A[j] * b

print(*B[::-1])