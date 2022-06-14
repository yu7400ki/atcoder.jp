S = input()

cnt = 0
ans = 0
for s in S:
    if s == 'B':
        cnt += 1
    elif s =='W':
        ans += cnt

print(ans)