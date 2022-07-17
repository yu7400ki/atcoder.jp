N, X, Y, Z = map(int, input().split())
A = [(n, i) for i, n in enumerate(list(map(int,input().split())))]
B = [(n, i) for i, n in enumerate(list(map(int,input().split())))]
C = [(A[i][0] + B[i][0], i) for i in range(N)]


A.sort(key = lambda x: x[0], reverse=True)
B.sort(key = lambda x: x[0], reverse=True)
C.sort(key = lambda x: x[0], reverse=True)

ans = []
ans_set = set()

for i in range(X):
    ans.append(A[i][1])
    ans_set.add(A[i][1])

j = 0
idx = 0
while j < Y:
    if B[idx][1] not in ans_set:
        ans.append(B[idx][1])
        ans_set.add(B[idx][1])
        j += 1
    idx += 1

idx = 0
k = 0
while k < Z:
    if C[idx][1] not in ans_set:
        ans.append(C[idx][1])
        ans_set.add(C[idx][1])
        k += 1
    idx += 1

ans.sort()
for i in ans:
    print(i+1)