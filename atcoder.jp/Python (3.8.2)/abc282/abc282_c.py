N = int(input())
S = list(input())

flag = False

for i in range(N):
    if S[i] == '"':
        flag = not flag
    elif S[i] == "," and not flag:
        S[i] = "."


print(''.join(S))
