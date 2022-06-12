from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))

cnt = defaultdict(int)
for a in A:
	cnt[a] += 1

ans = 0
for x in range(10**5+1):
	ans = max(ans, cnt[x-1] + cnt[x] + cnt[x+1])

print(ans)