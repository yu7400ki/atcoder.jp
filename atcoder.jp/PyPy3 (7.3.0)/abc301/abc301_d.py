S = list(input())
N = int(input())

min_s = "".join(S).replace("?", "0")

if int(min_s, 2) > N:
    print(-1)
    exit()

def dfs(s, i = 0):
    num = int("".join(s).replace("?", "0"), 2)
    if num > N:
        return "0"
    if i == len(S):
        return "".join(s)
    if S[i] == "?":
        s[i] = "1"
        l = dfs(s, i + 1)
        s[i] = "0"
        r = dfs(s, i + 1)
        s[i] = "?"
        res = max(l, r, key=lambda x: int(x, 2))
    else:
        res = dfs(s, i + 1)
    return res

print(int(dfs(S), 2))
