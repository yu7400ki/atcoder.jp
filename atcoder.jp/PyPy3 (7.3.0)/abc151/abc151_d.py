from collections import defaultdict, deque

H, W = map(int, input().split())
S = [list("#" * (W + 2))] + [list("#" + input() + "#") for _ in range(H)] + [list("#" * (W + 2))]

ans = 0
for y1 in range(1, H + 1):
    for x1 in range(1, W + 1):
        for y2 in range(1, H + 1):
            for x2 in range(1, W + 1):
                s = (y1, x1)
                e = (y2, x2)

                if S[y1][x1] == "#" or S[y2][x2] == "#":
                    continue

                depth = defaultdict(lambda : -1)
                depth[s] = 0
                queue = deque([s])

                while queue:
                    u = queue.popleft()
                    for v in [(u[0] + 1, u[1]), (u[0] - 1, u[1]), (u[0], u[1] + 1), (u[0], u[1] - 1)]:
                        if S[v[0]][v[1]] == "#" or depth[v] != -1:
                            continue
                        queue.append(v)
                        depth[v] = depth[u] + 1

                ans = max(ans, depth[e])

print(ans)
