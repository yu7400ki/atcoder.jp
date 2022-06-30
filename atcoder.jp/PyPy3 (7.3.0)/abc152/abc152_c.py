N = int(input())
P = list(map(int,input().split()))

ans = 0
mi = float('inf')
for i in P:
    mi = min(mi,i)
    if i <= mi:
        ans += 1

print(ans)