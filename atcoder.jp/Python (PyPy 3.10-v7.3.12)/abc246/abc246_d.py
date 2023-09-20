N = int(input())

def f(a, b):
    return a ** 3 + a**2*b + a*b**2 + b**3

b = 10 ** 6
ans = float("inf")

for a in range(10**6 + 1):
    while f(a, b) >= N and b >= 0:
        ans = min(ans, f(a, b))
        b -= 1

print(ans)
