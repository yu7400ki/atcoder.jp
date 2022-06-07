N = int(input())

sum_aoki = 0
aoki = [0] * N
AB = [[]] * N
for i in range(N):
	a, b = map(int,input().split())
	sum_aoki += a
	aoki[i] = a
	AB[i] = [a + b, i]

AB.sort(reverse=True, key=lambda x: x[0])

ans = 0
takahashi = 0
for num, idx in AB:
	ans += 1
	sum_aoki -= aoki[idx]
	takahashi += num
	if takahashi > sum_aoki:
		break

print(ans)