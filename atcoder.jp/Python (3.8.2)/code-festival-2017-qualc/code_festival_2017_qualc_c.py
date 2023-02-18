S = list(input())

ans = 0
T = []
for s in S:
    if s == "x":
        ans += 1
    else:
        T.append(s)

if T != T[::-1]:
    ans = -1

print(ans)
