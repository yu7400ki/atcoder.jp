n = int(input())
bb = [int(i) for i in input().split()]

l = []
c = 0
for j in bb:
	if j % 2==0:
		l.append(j//2)
	if len(l) == n:
		c+=1
		bb.extend(l)
		l = []
		
print(c)