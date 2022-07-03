from sys import stdin
input = lambda : stdin.readline().rstrip()

N, X = map(int,input().split())

ans = float('inf')
T = 0
for i in range(1, (N if N < X else X)+1):
    A, B = map(int,input().split())
    T += A + B
    res = T + (X - i) * B
    ans = res if res < ans else ans

print(ans)