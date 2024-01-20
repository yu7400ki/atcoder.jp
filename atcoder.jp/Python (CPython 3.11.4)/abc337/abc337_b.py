import itertools

S = [[key,len(list(group))] for key,group in itertools.groupby(list(input()))]
if len(S) > 3:
    print("No")
else:
    for s, t in zip(S, ["A", "B", "C"]):
        if s[0] != t:
            print("No")
            break
    else:
        print("Yes")
