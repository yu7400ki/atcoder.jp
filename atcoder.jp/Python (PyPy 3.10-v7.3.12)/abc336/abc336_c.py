def base5(n):
    if n == 0:
        return "0"
    res = []
    while n:
        res.append(str(n % 5))
        n //= 5
    res.reverse()
    return "".join(res)

N = int(input()) - 1
print(*[int(i) * 2 for i in base5(N)], sep="")
