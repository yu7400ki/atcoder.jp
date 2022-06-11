H, W = map(int,input().split())
s = [['.']+list(input())+['.'] for _ in range(H)]
s = [['.'] * (W+2)] + s + [['.'] * (W+2)]

ans = True
for i in range(1,H+1):
	for j in range(1,W+1):
		if s[i][j] == '#':
			if '#' not in [s[i+1][j],s[i-1][j],s[i][j+1],s[i][j-1]]:
				ans = False

print('Yes' if ans else 'No')