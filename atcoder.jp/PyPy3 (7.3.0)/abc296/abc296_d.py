from math import ceil

N, M = map(int, input().split())

def divisors(n):
    upper, lower = [], []
    for i in range(1, ceil(n**0.5)+1):
        lower.append(i)
        upper.append(n // i)
    return lower, upper

lower, upper = divisors(M)

ans = []

for l, u in zip(lower, upper):
    if l > N or u > N:
        continue

    if l * u >= M:
        ans.append(l * u)

    if l < N:
        if (l + 1) * u >= M:
            ans.append((l + 1) * u)

    if u < N:
        if l * (u + 1) >= M:
            ans.append(l * (u + 1))

    if l < N and u < N:
        if (l + 1) * (u + 1) >= M:
            ans.append((l + 1) * (u + 1))

if ans:
    print(min(ans))
else:
    print(-1)
