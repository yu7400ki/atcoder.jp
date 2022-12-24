S = list(input())
N = len(S)

box = set()

for i in range(N):
    if S[i] == "(":
        pass
    elif S[i] == ")":
        box.clear()
    else:
        if S[i] in box:
            print("No")
            exit()
        else:
            box.add(S[i])

print("Yes")
