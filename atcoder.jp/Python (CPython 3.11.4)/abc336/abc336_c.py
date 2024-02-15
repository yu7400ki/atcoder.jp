def to_base5(n):
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res = str(n % 5) + res
        n //= 5
    return res


N = int(input()) - 1

print(*[int(x) * 2 for x in to_base5(N)], sep="")
