from collections import defaultdict

dic = defaultdict(int)

N = int(input())
for _ in range(N):
	dic[input()] += 1

M = int(input())
for _ in range(M):
	dic[input()] -= 1

ans = dic[max(dic, key=lambda x: dic[x])]
print(ans if ans > 0 else 0)