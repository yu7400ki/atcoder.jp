N, X = map(int,input().split())

X *= 100
A = 0
cnt = 0

for _ in range(N):
    cnt += 1
    V, P = map(int,input().split())
    A += V * P
    if A > X:
        print(cnt)
        break
else:
    print(-1)