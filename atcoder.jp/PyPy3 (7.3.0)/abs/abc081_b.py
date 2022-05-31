input()
a = list(map(int,input().split()))
cnt = 0
while all(map(lambda x: x >> cnt & 1 == 0, a)):
	cnt += 1
print(cnt)