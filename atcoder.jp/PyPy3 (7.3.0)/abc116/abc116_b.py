s = int(input())

def f(n):
    if n % 2:
        return 3 * n + 1
    else:
        return n / 2

a = [s]
memo = set()
memo.add(s)

i = 1
while True:
    an = f(a[i-1])
    if an in memo:
        break
    a.append(an)
    memo.add(an)
    i += 1

print(i+1)