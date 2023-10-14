def prime_factorize(n):
    res = []
    while n & 1 == 0:
        res.append(2)
        n >>= 1
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            res.append(i)
            n //= i
    if n != 1:
        res.append(n)
    return res

N = int(input())

if N == 1:
    print("Yes")
else:
    A = prime_factorize(N)
    if set(A) in [{2}, {3}, {2, 3}]:
        print("Yes")
    else:
        print("No")
