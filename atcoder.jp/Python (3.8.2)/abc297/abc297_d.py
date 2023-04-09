import sys
sys.setrecursionlimit(1000000)

def gcd(a, b, ans = 0):
    if b == 0:
        return ans
    else:
        return gcd(b, a % b, ans + a // b)

A, B = map(int, input().split())

ans = gcd(A, B)

print(ans - 1)
