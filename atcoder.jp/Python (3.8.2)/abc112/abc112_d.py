def divisors(n):
    lower_divisors , upper_divisors = [], []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            lower_divisors.append(i)
            if n // i != i:
                upper_divisors.append(n // i)
    return lower_divisors + upper_divisors[::-1]

N, M = map(int, input().split())

d = divisors(M)
filtered = filter(lambda x: x <= M / N, d)
ans = max(filtered)

print(ans)
