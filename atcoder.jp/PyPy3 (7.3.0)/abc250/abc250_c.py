n,q = map(int,input().split())
ball = list(range(1,n+1))
index = [-1] + list(range(n))

for _ in range(q):
	x = int(input())
	i = index[x]
	if i == n-1:
		i -= 1
	index[ball[i]], index[ball[i+1]] = index[ball[i+1]], index[ball[i]]
	ball[i], ball[i + 1] = ball[i + 1], ball[i]

print(*ball)