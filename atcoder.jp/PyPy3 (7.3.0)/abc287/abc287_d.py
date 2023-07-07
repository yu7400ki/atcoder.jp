S = list(input())
T = list(input())

x = len(T)
match_head = [False] * (x + 1)
match_tail = [False] * (x + 1)
match_head[0] = True
match_tail[0] = True

for i in range(x):
    if S[i] == T[i] or S[i] == "?" or T[i] == "?":
        match_head[i + 1] = True
    else:
        break

for i in range(x):
    if S[-(i + 1)] == T[-(i + 1)] or S[-(i + 1)] == "?" or T[-(i + 1)] == "?":
        match_tail[i + 1] = True
    else:
        break

for i in range(x + 1):
    if match_head[i] and match_tail[x - i]:
        print("Yes")
    else:
        print("No")
