import sys

#sys.setrecursionlimit(10**8)

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
		for i in range(1,d):
			if c_1 != int(c[(l//d)*i : l//d*(d+1)]):
				if c_1 > int(c[(l//d)*i : l//d*(d+1)]):
					c_1 -= 1
				break
		if len(str(c_1)) < (l//d):
			c_1 = '9' * (l-1)
			return c_1
		ans = str(c_1) * d
	else:
		c_1 = int(c[0])
		for i in range(1,l):
			if c_1 != int(c[i]):
				if c_1 > int(c[i]):
					c_1 -= 1
				break
		if c_1 == 0:
			c_1 = 9
		ans = str(c_1) * l
		if int(ans) > int(c):
			ans = ans[1:]

	return ans

T = int(input())
for _ in range(T):
	print(main(input()))