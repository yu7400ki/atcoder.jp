N = int(input())
S = input()

def solve(s):
    res = 0
    tmp = 0
    if "o" not in s:
        return -1
    first = s.find("-")
    if first == -1:
        return 0
    for i in range(first + 1, N):
        if s[i] == "o":
            tmp += 1
        else:
            res = max(res, tmp)
            tmp = 0
    res = max(res, tmp)
    return res

ans = max(solve(S), solve(S[::-1]))

print(ans)
