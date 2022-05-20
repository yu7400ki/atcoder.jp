N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

hit = 0
for i in range(N):
    if A[i] == B[i]:
        hit += 1

blow = len(set(A) & set(B)) - hit

print(hit)
print(blow)