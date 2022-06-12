R, X, Y = map(int,input().split())

dist = (X ** 2 + Y ** 2) ** 0.5

if dist == R:
	print(1)
elif dist <= 2*R:
	print(2)
else:
	print(int(-(dist // -R)))