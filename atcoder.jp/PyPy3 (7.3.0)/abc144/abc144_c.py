N = int(input())

ans = float('INF')
for i in range(1,int(N**0.5) + 1):
    if N % i == 0:
        ans = min(ans, (i-1) + (N//i-1))

print(ans)