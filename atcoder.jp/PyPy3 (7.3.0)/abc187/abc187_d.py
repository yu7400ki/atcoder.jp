N = int(input())

X = 0
x = [0] * N
for i in range(N):
	A, B = map(int,input().split())
	X -= A
	x[i] = 2 * A + B

x.sort()

ans = 0
while X <= 0:
	X += x.pop()
	ans += 1

print(ans)