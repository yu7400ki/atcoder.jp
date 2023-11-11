S = input()
S = S.replace("AB", "D")
S = list(S)[::-1]

ans = []
while S:
    s = S.pop()
    if len(ans) == 0:
        ans.append(s)
    else:
        if ans[-1] == "D" and s == "C":
            ans.pop()
        elif ans[-1] == "A" and s == "B":
            ans.pop()
            ans.append("D")
        else:
            ans.append(s)

ans = "".join(ans)
ans = ans.replace("D", "AB")
print(ans)
