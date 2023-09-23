import sys
sys.setrecursionlimit(10**9)

K = int(input())

res = []
def dfs(n, ret=[]):
    ret.append(n)
    res.append(int("".join(map(str, ret))))
    if ret[-1] != 0:
        for i in range(n):
            dfs(i)
    ret.pop()

for i in range(10):
    dfs(i)

res.sort()
print(res[K])
