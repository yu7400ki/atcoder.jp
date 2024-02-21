N = list(map(int, list(input())))
l = len(N)
u = 9 * l + 1


def solve(s: int):
    dp = [[[[0] * 2 for _ in range(s)] for _ in range(s + 1)] for _ in range(l + 1)]
    dp[0][0][0][0] = 1

    for d in range(l):
        for i in range(s + 1):
            for j in range(s):
                for f in range(2):
                    for t in range(10 if f else N[d] + 1):
                        if i + t > s:
                            break
                        nd = d + 1
                        ni = i + t
                        nj = (10 * j + t) % s
                        nf = f or t < N[d]
                        dp[nd][ni][nj][nf] += dp[d][i][j][f]

    return dp[l][s][0][1] + dp[l][s][0][0]


ans = sum(solve(i) for i in range(1, u))
print(ans)
