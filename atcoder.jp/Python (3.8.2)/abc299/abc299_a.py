N = int(input())
S = input()

l = False
r = False

for i, s in enumerate(S):
    if s == "|":
        r = l
        l = True
    elif s == "*":
        if l and r:
            print("out")
        elif l:
            print("in")
        else:
            print("out")
