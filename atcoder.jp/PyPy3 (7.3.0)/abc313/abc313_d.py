from collections import deque, defaultdict

N, K = map(int, input().split())

bit = [i < K for i in range(N)]

def question(bit):
    q = "? " + " ".join(map(str, [i + 1 for i, b in enumerate(bit) if b]))
    print(q)

history = {}

start = 0
end = K
bit = deque([i < K for i in range(N)])
question(bit)
res = int(input())
current = tuple(bit)
history[current] = res

different = {}
graph = defaultdict(list)
for i in range(N):
    prev = current
    bit[start] = False
    bit[end] = True
    question(bit)
    res = int(input())
    current = tuple(bit)
    history[current] = res
    # graph[start] = (end, history[current] == history[prev])
    graph[start].append(end)
    different[(start, end)] = history[current] != history[prev]
    start = (start + 1) % N
    end = (end + 1) % N

ans = [0] * N
ans[0] = 1

def bfs(graph, n):
    depth = defaultdict(lambda: -1)
    depth[n] = 0
    queue = deque()
    queue.append(n)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] == -1:
                queue.append(v)
                depth[v] = depth[u] + 1
                if different[(u, v)]:
                    ans[v] = 1 - ans[u]
                else:
                    ans[v] = ans[u]

    return depth

depth = bfs(graph, 0)

sum_ans = 0
for idx, b in enumerate(prev):
    if b:
        sum_ans += ans[idx]

if sum_ans % 2 != history[prev]:
    ans = [1 - a for a in ans]

print("! " + " ".join(map(str, ans)))
