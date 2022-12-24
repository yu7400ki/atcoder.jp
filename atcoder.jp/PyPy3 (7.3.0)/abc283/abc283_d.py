S = input()
N = len(S)

def binary_search(lst, target, ok = -1, ng = None, key = None):
    ng = len(lst) if ng is None else ng
    key = (lambda x: lst[x] <= target) if key is None else key

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if key(mid):
            ok = mid
        else:
            ng = mid

    return ok


box = set()
box_accum = [set()]

open_accum = [0]
for i in range(N):
    if S[i] == "(":
        open_accum.append(open_accum[-1] + 1)
    elif S[i] == ")":
        open_accum.append(open_accum[-1])
    else:
        open_accum.append(open_accum[-1])

close_cnt = 0

for i in range(N):
    if S[i] == "(":
        box_copy = box_accum[-1].copy()
        box_accum.append(box_copy)
    elif S[i] == ")":
        close_cnt += 1
        box_copy = box_accum[-1].copy()
        box_accum.append(box_copy)

        ok = binary_search(open_accum, open_accum[i] - close_cnt)

        delete_box = box_accum[i] - box_accum[ok]
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
