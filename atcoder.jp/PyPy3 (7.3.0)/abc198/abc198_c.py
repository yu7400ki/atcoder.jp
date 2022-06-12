R, X, Y = map(int,input().split())

dist = (X ** 2 + Y ** 2) ** 0.5

if dist > R:
	print(int(-(dist // -R)))
else:
	print(2)