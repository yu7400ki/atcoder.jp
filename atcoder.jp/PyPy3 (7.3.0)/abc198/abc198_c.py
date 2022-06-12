R, X, Y = map(int,input().split())

dist = (X ** 2 + Y ** 2) ** 0.5

print(int(-(dist // -R)))