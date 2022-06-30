N, X = map(int,input().split())

X *= 100
A = 0

for i in range(N):
    V, P = map(int,input().split())
    A += V * P
    if A > X:
        print(i + 1)
        break
else:
    print(-1)