from collections import defaultdict

N = int(input())
S = list(input())

history = defaultdict(int)

prev = S.pop()
n = 1
history[prev] = n
ans = 1

while S:
    s = S.pop()
    if s == prev:
        n += 1
    else:
        n = 1
    if n > history[s]:
        ans += 1
        history[s] = n
    prev = s

print(ans)
