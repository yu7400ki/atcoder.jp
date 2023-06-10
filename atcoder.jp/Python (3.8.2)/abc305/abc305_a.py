N = int(input())

m = N % 5
d = min(m, m - 5, key=abs)

print(N - d)
