import sys
sys.setrecursionlimit(10**6)

s = list(input())
t = list(input())

dp = [[-1] * (len(s) + 1) for _ in range(len(t) + 1)]
dp[0] = [0] * (len(s) + 1)
for i in range(len(t) + 1):
    dp[i][0] = 0

for i in range(1, len(t)+1):
    for j in range(1, len(s)+1):
        if t[i-1] == s[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

def restore(dp, s_pos, t_pos, ret = None):
    ret = ret or []
    if s_pos == 0 and t_pos == 0:
        return ret
    transitioned = False
    if s_pos != 0:
        if dp[t_pos][s_pos-1] == dp[t_pos][s_pos]:
            transitioned = True
            ret = restore(dp, s_pos-1, t_pos, ret)
    if t_pos != 0 and not transitioned:
        if dp[t_pos-1][s_pos] == dp[t_pos][s_pos]:
            transitioned = True
            ret = restore(dp, s_pos, t_pos-1, ret)
    if not transitioned:
        ret.append(s[s_pos-1])
        ret = restore(dp, s_pos-1, t_pos-1, ret)
    return ret

ans = restore(dp, len(s), len(t))
print("".join(ans[::-1]))
