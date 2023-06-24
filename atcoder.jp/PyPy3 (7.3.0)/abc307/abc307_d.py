N = int(input())
S = list(input())

ans = []
open_bracket = 0
for s in S:
    if s == "(":
        open_bracket += 1
        ans.append(s)
    elif s == ")":
        if open_bracket > 0:
            while True:
                t = ans.pop()
                if t == "(":
                    break
            open_bracket -= 1
        else:
            ans.append(s)
    else:
        ans.append(s)

print("".join(ans))
