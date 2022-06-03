N = int(input())

def g(x,y,z):
	return x**2 + y**2 + z**2 + x*y + y*z + z*x

def f(n):
	limit = int(n**0.5) + 2
	cnt = 0
	for x in range(1,limit):
		for y in range(1,limit):
			ok = 0
			ng = limit
			while ng - ok > 1:
				mid = (ok + ng) // 2
				if g(x,y,mid) <= n:
					ok = mid
				else:
					ng = mid
			if ok != 0:
				if g(x,y,ok) == n:
					cnt += 1
	return cnt

for i in range(1,N+1):
	print(f(i))