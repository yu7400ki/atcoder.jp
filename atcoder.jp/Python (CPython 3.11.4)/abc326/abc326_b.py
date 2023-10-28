def is_326like(n):
    a = int(str(n)[0])
    b = int(str(n)[1])
    c = int(str(n)[2])
    return a * b == c


N = int(input())

for i in range(N, 1000):
    if is_326like(i):
        print(i)
        break
