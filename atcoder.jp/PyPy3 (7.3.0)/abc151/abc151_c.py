from collections import defaultdict

N, M = map(int,input().split())

ac = set()
wa = defaultdict(int)
ac_cnt = 0
wa_cnt = 0

for i in range(M):
	p, s = input().split()
	if p in ac:
		continue
	if s == 'AC':
		ac_cnt += 1
		ac.add(p)
	elif s == 'WA':
		wa[p] += 1

for j in wa:
	if j in ac:
		wa_cnt += wa[j]

print(ac_cnt, wa_cnt)