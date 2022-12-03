S = list(input())
T = list(input())

for i in range(len(S)):
    if S[i] == T[i]:
        continue
    else:
        print(i+1)
        break
