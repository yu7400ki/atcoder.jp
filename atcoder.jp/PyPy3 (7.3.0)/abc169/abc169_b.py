N = int(input())
A = list(map(int,input().split()))
LIMIT = 10**18

if 0 in A:
	print(0)
	exit()

ans = 1
for a in A:
	ans *= a
	if ans > LIMIT:
		print(-1)
		exit()

print(ans)