n,q = map(int,input().split())
ball = list(range(1,n+1))
index = list(range(n))
for i in range(q):
	x = int(input())
	p = index[x-1]
	if p == n-1:
		p -= 1
	index[ball[p]-1], index[ball[p+1]-1] = index[ball[p+1]-1], index[ball[p]-1]
	ball[p], ball[p + 1] = ball[p + 1], ball[p]

print(*ball)