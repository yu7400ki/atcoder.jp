H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

ans = []
for i in range(W):
    cnt = 0
    for j in range(H):
        if C[j][i] == '#':
            cnt += 1
    ans.append(cnt)

print(*ans, sep=" ")
