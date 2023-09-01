N = int(input())

def dfs(c, ma):
    if len(c) == N:
        print(*[chr(ord("a") + i) for i in c], sep="")
    else:
        for i in range(ma + 1):
            dfs(c + [i], ma + 1 if i == ma else ma)

dfs([], 0)
