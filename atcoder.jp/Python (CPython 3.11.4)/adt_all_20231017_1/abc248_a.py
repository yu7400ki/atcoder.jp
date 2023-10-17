S = set(map(int, list(input())))

entire = set(range(10))
rest = entire - S

print(rest.pop())
