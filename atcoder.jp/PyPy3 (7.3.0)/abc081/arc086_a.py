from collections import defaultdict

N, K = map(int,input().split())
A = list(map(int,input().split()))

cnt = defaultdict(int)
for a in A:
    cnt[a] += 1

length = len(cnt)
num = [cnt[i] for i in cnt]
num.sort()

ans = 0
for i in range(length - K):
    ans += num[i]

print(ans)