S = input()
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
box_accum = [set()]

close_cnt = 0

for i in range(N):
    if S[i] == "(":
        box_copy = box_accum[-1].copy()
        box_accum.append(box_copy)
    elif S[i] == ")":
        idx = pair[i]
        box_copy = box_accum[-1].copy()
        box_accum.append(box_copy)

        delete_box = box_accum[i] - box_accum[idx]
        box -= delete_box
    else:
        if S[i] in box:
            print("No")
            exit()
        else:
            box.add(S[i])
            box_copy = box_accum[-1].copy()
            box_copy.add(S[i])
            box_accum.append(box_copy)

print("Yes")
