S = list(input())
N = len(S)


pair = {}
temp = []
for i in range(N):
    if S[i] == "(":
        temp.append(i)
    elif S[i] == ")":
        pair[temp.pop()] = i
pair = {v: k for k, v in pair.items()}


box = set()

for i in range(N):
    if S[i] == "(":
        pass
    elif S[i] == ")":
        idx = pair[i]

        box -= set(S[idx:i])
    else:
        if S[i] in box:
            print("No")
            exit()
        else:
            box.add(S[i])

print("Yes")
