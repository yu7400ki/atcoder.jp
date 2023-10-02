A, B = map(int, input().split())

def f(n):
    if n & 1 == 0:
        return (n + 1) >> 1 & 1 ^ n
    else:
        return (n + 1) >> 1 & 1

ans = f(A - 1) ^ f(B)
print(ans)
