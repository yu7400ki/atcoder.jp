from collections import defaultdict

N, K = map(int,input().split())
c = list(map(int,input().split()))

choose = defaultdict(int)

for i in range(K):
	choose[c[i]] += 1

ans = len(choose)
for i in range(K,N):
	choose[c[i-K]] -= 1
	choose[c[i]] += 1
	ans = max(ans, len(choose))

print(ans)