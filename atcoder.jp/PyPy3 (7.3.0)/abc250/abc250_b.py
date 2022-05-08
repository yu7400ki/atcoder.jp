n, a, b = map(int,input().split())

for k in range(n//2):
	for i in range(a):
		for j in range(n//2):
			print('.' * b + '#' * b, end='')
		if n % 2:
			print('.' * b, end='')
		print('')
	for i in range(a):
		for j in range(n//2):
			print('#' * b + '.' * b, end='')
		if n % 2:
			print('#' * b, end='')
		print('')
if n % 2:
	for i in range(a):
		for j in range(n//2):
			print('.' * b + '#' * b, end='')
		if n % 2:
			print('.' * b, end='')
		print('')