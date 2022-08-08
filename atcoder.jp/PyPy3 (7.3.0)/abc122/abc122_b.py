S = input()

cnt = 0
ans = 0
li = ['A', 'T', 'C', 'G']

for s in S:
    if s in li:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)