N = int(input())
S = list(input())

R = 0
L = 0
U = 0
D = 0

ans = "No"

for s in S:
    if s == 'R':
        R += 1
    elif s == 'L':
        L += 1
    elif s == 'U':
        U += 1
    elif s == 'D':
        D += 1
    if R == L and U == D:
        ans = "Yes"
        break

print(ans)
