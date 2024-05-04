S = list(input())
T = list(input())
S.reverse()
T.reverse()

ans = []
i = 0
while S:
    i += 1
    if S[-1] == T[-1]:
        S.pop()
        T.pop()
        ans.append(i)
    else:
        T.pop()

print(*ans)
