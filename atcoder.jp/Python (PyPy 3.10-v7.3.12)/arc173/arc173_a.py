def calc(x: int) -> int:
    s = str(x)
    n = len(s)
    dp = [[[0] * 2 for _ in range(11)] for _ in range(n + 5)]
    dp[1][10][1] = 1
    for j in range(1, int(s[0])):
        dp[1][j][1] = 1
    dp[1][int(s[0])][0] = 1
    for i in range(1, n):
        dp[i + 1][10][1] += dp[i][10][0] + dp[i][10][1]
        for j in range(1, 10):
            dp[i + 1][j][1] += dp[i][10][0] + dp[i][10][1]

        for j in range(10):
            for k in range(10):
                if j == k:
                    continue
                dp[i + 1][k][1] += dp[i][j][1]
                if k < int(s[i]):
                    dp[i + 1][k][1] += dp[i][j][0]
                elif k == int(s[i]):
                    dp[i + 1][k][0] += dp[i][j][0]
    ret = 0
    for j in range(10):
        ret += dp[n][j][0] + dp[n][j][1]
    return ret


def solve(k: int) -> int:
    ng = 0
    ok = 10**18
    while abs(ng - ok) > 1:
        mid = (ng + ok) // 2
        if calc(mid) >= k:
            ok = mid
        else:
            ng = mid
    return ok


T = int(input())
for _ in range(T):
    k = int(input())
    print(solve(k))
