H, W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

A_h = [sum(A[i]) for i in range(H)]
A_w = [sum([A[i][j] for i in range(H)]) for j in range(W)]

ans = [[A_h[i] + A_w[j] - A[i][j] for j in range(W)] for i in range(H)]
for h in ans:
	print(*h)