from sys import stdin
input = lambda : stdin.readline().rstrip()

N, X = map(int,input().split())
Y = min(N, X)
AB = [list(map(int,input().split())) for _ in range(Y)]

accum = [0] * (Y + 1)
for i, n in enumerate(AB):
    accum[i+1] = accum[i] + n[0] + n[1]

ans = float('inf')
for i in range(Y):
    i += 1
    a = accum[i]
    ans = min(a + (X - i) * AB[i-1][1], ans)

print(ans)