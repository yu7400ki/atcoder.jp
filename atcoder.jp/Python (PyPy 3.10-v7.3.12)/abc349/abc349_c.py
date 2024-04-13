S = input()
T = input().lower()


def check(s, t):
    i = 0
    for c in s:
        if c == t[i]:
            i += 1
            if i == len(t):
                return True
    return False


if T.endswith("x"):
    res = check(S, T[:2])
else:
    res = check(S, T)

print("Yes" if res else "No")
