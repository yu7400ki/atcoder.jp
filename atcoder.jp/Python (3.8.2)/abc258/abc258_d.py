from sys import stdin
input = lambda : stdin.readline().rstrip()

N, X = map(int,input().split())

ans = float('inf')
T = 0
for i in range(1, min(N,X)+1):
    A, B = map(int,input().split())
    T += A + B
    ans = min(T + (X - i) * B, ans)

print(ans)