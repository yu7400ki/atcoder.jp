S = list(input())
T = list(input())

ans = []

for i in range(max(len(S) - len(T) + 1, 0)):
    for j in range(len(T)):
        if S[i + j] != "?" and S[i + j] != T[j]:
            break
    else:
        candidate = S[:i] + T + S[i + len(T):]
        ans.append("".join(candidate).replace("?", "a"))

ans.sort()

if ans:
    print(ans[0])
else:
    print("UNRESTORABLE")
