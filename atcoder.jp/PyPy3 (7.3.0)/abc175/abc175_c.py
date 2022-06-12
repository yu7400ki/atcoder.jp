X, K, D = map(int,input().split())

X = abs(X)
if X // D <= K:
	d = X // D
	X -= d * D
	K -= d
else:
	X -= K * D
	K = 0

if K > 0:
	positive = X
	negative = X - D
	if K % 2:
		print(abs(negative))
	else:
		print(positive)
else:
	print(X)