import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
connect = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    connect[a-1].append(b-1)
    connect[b-1].append(a-1)

surface = list(map(int, input().split()))

def dfs(now, visited, visited_all = [False] * N):
    if visited[now]:
        return True
    visited[now] = True
    if visited_all[now]:
        return False
    visited_all[now] = True

    ret = False
    for next in connect[now]:
        if surface[now] != surface[next]:
            surface[now] = not surface[now]
            ret |= dfs(next, visited)
            surface[now] = not surface[now]
    visited[now] = False

    return ret

for n in range(N):
    if dfs(n, [False] * N):
        print("Yes")
        break
else:
    print("No")
