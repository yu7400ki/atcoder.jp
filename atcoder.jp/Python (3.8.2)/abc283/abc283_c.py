S = list(input())

ans = 0
while S:
    if S[-2:] == ['0', '0']:
        S.pop()
        S.pop()
        ans += 1
    else:
        S.pop()
        ans += 1

print(ans)
