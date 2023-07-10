import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
connect = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    connect[a-1].append(b-1)
    connect[b-1].append(a-1)
surface = list(map(int, input().split()))

def dfs(now, visited = None, visited_all = set()):
    visited = visited or set()
    if now in visited:
        return True
    visited.add(now)
    if now in visited_all:
        return False
    visited_all.add(now)

    ret = False
    for next in connect[now]:
        surface[now] = not surface[now]
        if surface[now] != surface[next] and next not in visited:
            ret |= dfs(next, visited)
        elif surface[now] == surface[next] and next in visited:
            ret |= dfs(next, visited)
        surface[now] = not surface[now]
    visited.discard(now)

    return ret

for n in range(N):
    if dfs(n, set()):
        print("Yes")
        break
else:
    print("No")
