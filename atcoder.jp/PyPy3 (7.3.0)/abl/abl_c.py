N, M = map(int,input().split())
ct = set(range(1,N+1))
for i in range(M):
    A, B = map(int,input().split())
    ct.discard(A)
    ct.discard(B)

print(len(ct))