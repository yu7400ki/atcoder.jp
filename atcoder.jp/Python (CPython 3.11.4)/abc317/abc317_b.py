N = int(input())
A = list(map(int, input().split()))

A = set(A)
mi = min(A)
entire = set(range(mi, mi + N))
rest = entire - A

print(rest.pop())
