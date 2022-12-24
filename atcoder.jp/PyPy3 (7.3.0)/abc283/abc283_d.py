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


box_accum = [set()]
for i in range(N):
    if S[i] == "(":
        copy = box_accum[-1].copy()
        box_accum.append(copy)
    elif S[i] == ")":
        copy = box_accum[-1].copy()
        box_accum.append(copy)
    else:
        copy = box_accum[-1].copy()
        copy.add(S[i])
        box_accum.append(copy)


box = set()

for i in range(N):
    if S[i] == "(":
        pass
    elif S[i] == ")":
        idx = pair[i]

        delete = box_accum[i] - box_accum[idx]
        box -= delete
    else:
        if S[i] in box:
            print("No")
            exit()
        else:
            box.add(S[i])

print("Yes")
