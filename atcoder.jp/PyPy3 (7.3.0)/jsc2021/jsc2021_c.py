from pickle import TRUE


A, B = map(int,input().split())
ans = 1
for i in range(1,B+1):
	if -(-A // i) < (B // i):
		ans = i
print(ans)