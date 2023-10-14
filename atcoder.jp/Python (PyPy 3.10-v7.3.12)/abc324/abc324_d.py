from collections import Counter

N = int(input())
S = input()

ma = int("".join(sorted(S, reverse=True)))
cnt = Counter(S)

ans = 0
for i in range(3162278):
    n = i * i
    if n > ma:
        break
    n = Counter(f"{n:013}"[13-N:])
    if n == cnt:
        ans += 1

print(ans)
