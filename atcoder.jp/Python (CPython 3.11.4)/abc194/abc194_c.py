from collections import Counter

N = int(input())
A = list(map(int, input().split()))

ans = 0
cnt = Counter(A)
keys = list(cnt.keys())
n = len(keys)
for i in range(n):
    for j in range(i+1, n):
        ans += (keys[i] - keys[j]) ** 2 * (cnt[keys[i]] * cnt[keys[j]])

print(ans)
