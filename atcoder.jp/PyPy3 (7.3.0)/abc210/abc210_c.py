from collections import defaultdict

N, K = map(int,input().split())
c = list(map(int,input().split()))

choose = defaultdict(int)

for i in range(K):
	choose[c[i]] += 1

ans = len(choose)
length = ans
for i in range(K,N):
	choose[c[i-K]] -= 1
	if choose[c[i-K]] == 0:
		length -= 1
	choose[c[i]] += 1
	if choose[c[i]] == 1:
		length += 1
	ans = max(ans, length)

print(ans)