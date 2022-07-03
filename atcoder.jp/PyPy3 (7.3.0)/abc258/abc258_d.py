N, X = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]

accum = [0] * (N + 1)
for i, n in enumerate(AB):
    accum[i+1] = accum[i] + n[0] + n[1]

ans = float('inf')
for i in range(min(N, X)):
    i += 1
    a = accum[i]
    ans = min(a + (X - i) * AB[i-1][1], ans)

print(ans)