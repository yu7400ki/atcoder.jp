from collections import defaultdict

N, M, T = map(int,input().split())
A = list(map(int,input().split()))
XY = defaultdict(int)
for _ in range(M):
    X, Y = map(int,input().split())
    XY[X] = Y

for i in range(N-1):
    if A[i] < T:
        T -= A[i]
    else:
        print('No')
        break
    T += XY[i+2]
else:
    print('Yes')