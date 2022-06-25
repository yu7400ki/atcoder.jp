N = int(input())
S = list(map(int,list(input())))
W = list(map(int,input().split()))

w = []
for i in range(N):
	w.append((S[i], W[i]))

w.sort(key=lambda x:x[1])

child = [0]
adult = [0]
for i, n in enumerate(w):
	if n[0] == 0:
		child.append(child[-1] + 1)
		adult.append(adult[-1])

	else:
		adult.append(adult[-1] + 1)
		child.append(child[-1])

ans = max(adult[-1], child[-1])
for i in range(N):
	ans = max(ans, child[i] + adult[-1] - adult[i])

print(ans)