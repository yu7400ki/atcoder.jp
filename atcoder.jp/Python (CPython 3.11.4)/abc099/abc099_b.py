a, b = map(int, input().split())

diff = b - a
print(sum(range(diff)) - a)
