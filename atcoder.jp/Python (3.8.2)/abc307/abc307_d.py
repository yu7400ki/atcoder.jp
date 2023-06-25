N = int(input())
S = input()

tempList, ans, removed = [], [], 0
for s in range(N):
    if S[s] == "(":
        ans.append(S[s])
        tempList.append(s - removed)
    elif S[s] == ")":
        if len(tempList) != 0:
            t = tempList.pop()
            for _ in range(len(ans) - t):
                ans.pop()
            removed = s - t + 1
        else:
            ans.append(S[s])
    else:
        ans.append(S[s])

print("".join(ans))
