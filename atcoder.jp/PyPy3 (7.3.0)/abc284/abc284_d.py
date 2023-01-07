T = int(input())

def solve(n):
    if n % 2 == 0:
        a = 2
        b = (n // 2) ** 0.5
        if b.is_integer():
            return (int(b), a)
    if n % 4 == 0:
        b = 2
        a = n / b ** 2
        if a.is_integer():
            return (b, int(a))


    d = 3
    while True:
        if n % d == 0:
            a = d
            b = (n // d) ** 0.5
            if b.is_integer():
                return (int(b), a)

        if n % (d ** 2) == 0:
            b = d
            a = n / b ** 2
            if a.is_integer():
                return (b, int(a))

        d += 2

for _ in range(T):
    N = int(input())
    (a, b) = solve(N)
    print(a, b)
