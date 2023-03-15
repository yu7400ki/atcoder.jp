from itertools import product

N = int(input())

l = [3, 5, 7]
ans = 0

for i in range(1, 10):
    for p in product(l, repeat=i):
        if len(set(p)) != 3:
            continue
        x = int("".join(map(str, p)))
        if x <= N:
            ans += 1

print(ans)
