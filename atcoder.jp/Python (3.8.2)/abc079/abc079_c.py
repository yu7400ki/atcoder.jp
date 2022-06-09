ABCD = list(map(int,list(input())))

for i in range(1,2**3):
	res = ABCD[0]
	ans = [str(ABCD[0])]
	for j in range(3):
		if i >> j & 1:
			res += ABCD[j+1]
			ans.extend(['+', str(ABCD[j+1])])
		else:
			res -= ABCD[j+1]
			ans.extend(['-', str(ABCD[j+1])])
	if res == 7:
		ans.append('=7')
		print(''.join(ans))
		exit()