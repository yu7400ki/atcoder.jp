from collections import Counter

S = list(input())

cnt = Counter(S)

ans = 0 + any(v > 1 for v in cnt.values())
for s in S:
    cnt[s] -= 1
    for k, v in cnt.items():
        if k == s:
            continue
        ans += v

print(ans)
