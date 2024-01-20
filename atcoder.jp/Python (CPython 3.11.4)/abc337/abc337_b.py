S = list(input())
for s, t in zip(S, S[1:]):
    if s > t:
        print("No")
        break
else:
    print("Yes")
