n,q = map(int,input().split())
ball = list(range(1,n+1))
for i in range(q):
	x = int(input())
	index = ball.index(x)
	if index == n-1:
		ball[-2], ball[-1] = ball[-1], ball[-2]
	else:
		ball[index], ball[index + 1] = ball[index + 1], ball[index]

print(*ball)