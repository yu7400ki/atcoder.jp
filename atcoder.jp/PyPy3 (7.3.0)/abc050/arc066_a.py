from collections import Counter

N = int(input())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

def pow(n, p):
    res = 1
    for _ in range(p):
        res *= n
        res %= MOD
    return res

flag = True
if N % 2:
    if any(a % 2 for a in A):
        flag = False
    c = Counter(A)
    if 0 not in c or c[0] != 1:
        flag = False
    if any(v != 2 for k, v in c.items() if k != 0):
        flag = False
else:
    if any(a % 2 == 0 for a in A):
        flag = False
    c = Counter(A)
    if any(v != 2 for v in c.values()):
        flag = False

if flag:
    print(pow(2, N // 2))
else:
    print(0)
