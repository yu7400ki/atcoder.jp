from collections import deque

S = deque(input())

ans = 0

while len(S) > 1:
    if S[0] == S[-1]:
        S.popleft()
        S.pop()
    elif S[0] == "x":
        S.popleft()
        ans += 1
    elif S[-1] == "x":
        S.pop()
        ans += 1
    else:
        ans = -1
        break

print(ans)
