H, W = map(int,input().split())
S = [list(input()) for _ in range(H)]

ans = 0
for v in S:
    ans += v.count("#")

print(ans)