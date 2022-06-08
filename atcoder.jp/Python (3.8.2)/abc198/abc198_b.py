N = input()
limit = len(N)
for i in range(limit):
	res = '0' * i + N
	if res == res[::-1]:
		print('Yes')
		break
else:
	print('No')