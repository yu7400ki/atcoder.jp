N = int(input())
S = {}
T = []

for i in range(N):
	s,t = input().split()
	if s not in S:
		S[s] = i
	T.append(int(t))

num = 0
ans = 0
for i in S.values():
	if T[i] > num:
		num = T[i]
		ans = i + 1

print(ans)