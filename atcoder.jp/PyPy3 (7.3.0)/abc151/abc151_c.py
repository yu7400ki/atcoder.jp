N, M = map(int,input().split())

ac = set()
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
		wa_cnt += 1

print(ac_cnt, wa_cnt)