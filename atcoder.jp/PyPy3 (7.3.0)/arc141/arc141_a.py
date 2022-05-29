def f(n):
	for i in range(1,int(n**0.5)+1):
		if n % i == 0:
			ans = i
	return ans

def main(c):
	l = len(c)
	d = f(l)
	if d != 1:
		c_1 = int(c[:l//d])
		c_2 = int(c[l//d:l//d*2])
		if c_1 > c_2:
			c_1 -= 1
		if len(str(c_1)) < d:
			c_1 = '9' * d
		ans = str(c_1) * d
	else:
		c_1 = int(c[0])
		c_2 = int(c[1])
		if c_1 > c_2:
			c_1 -= 1
		if c_1 == 0:
			c_1 = 9
		ans = str(c_1) * l

	if int(ans) > int(c):
		ans = main(str(int(c)-1))
	return ans

T = int(input())
for _ in range(T):
	print(main(input()))