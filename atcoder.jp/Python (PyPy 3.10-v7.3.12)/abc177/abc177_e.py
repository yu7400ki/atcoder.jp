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
A = list(map(int, input().split()))

A_fact = [0] * N
for i in range(N):
    A_fact[i] = set(prime_factorize(A[i]))

is_pairwise = True
is_setwise = False

s = set()
for fact in A_fact:
    if s & fact:
        is_pairwise = False
        break
    s |= fact

s = set(A_fact[0])
for fact in A_fact:
    s &= fact
if not s:
    is_setwise = True

if is_pairwise:
    print("pairwise coprime")
elif is_setwise:
    print("setwise coprime")
else:
    print("not coprime")
