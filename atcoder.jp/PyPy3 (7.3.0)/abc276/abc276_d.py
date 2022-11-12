from functools import reduce

N = int(input())
A = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def count(x):
    cnt = 0
    while x % 2 == 0:
        x //= 2
        cnt += 1
    while x % 3 == 0:
        x //= 3
        cnt += 1
    return x, cnt

g = reduce(gcd, A)
A = map(lambda x: x // g, A)

ans = 0
for a in A:
    d, cnt = count(a)
    if d != 1:
        print(-1)
        exit()
    ans += cnt

print(ans)
