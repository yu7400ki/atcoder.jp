import itertools

S = [[key,len(list(group))] for key,group in itertools.groupby(list(input()))]
if len(S) > 3:
    print("No")
else:
    for s, t in zip(S, S[1:]):
        if s[0] > t[0]:
            print("No")
            break
    else:
        print("Yes")
