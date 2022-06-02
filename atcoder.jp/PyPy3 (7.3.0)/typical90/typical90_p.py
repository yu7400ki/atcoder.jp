N = int(input())
A, B, C = map(int,input().split())

LIMIT = 9999

ans = float('INF')
for i in range(LIMIT+1):
    for j in range(LIMIT+1-i):
        m = A*i + B*j
        if m <= N:
            k = (N - m) // C
            if m + C * k == N:
                ans = min(ans, i + j + k)
print(ans)