from sys import stdin
input = lambda : stdin.readline().rstrip()

N, X = map(int,input().split())

ans = float('inf')
T = 0
for i in range(min(N, X)):
    A, B = map(int,input().split())
    T += A + B
    ans = min(T + (X - i - 1) * B, ans)

print(ans)