h,w = map(int,input().split())
r,c = map(int,input().split())

if h * w == 1:
	print(0)
	exit()

if h == 1 or w == 1:
	cnt = 1
else:
	cnt = 2

if 1 < r < h:
	cnt += 1
if 1 < c < w:
	cnt += 1

print(cnt)