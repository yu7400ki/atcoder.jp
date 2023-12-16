N = int(input())

candidates = set()

for i in range(1, 20):
    for j in range(1, 20):
        for k in range(1, 20):
            a = int("1" * i)
            b = int("1" * j)
            c = int("1" * k)
            candidates.add(a + b + c)

candidates = sorted(list(candidates))
print(candidates[N - 1])
