from collections import deque, defaultdict

N, M, E = map(int, input().split())

graph = defaultdict(list)
li = [0] * E
for i in range(E):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)
    li[i] = (U, V)

def bfs(n):
    dic = defaultdict(lambda : -1)
    queue = deque()
    queue.append(n)
    dic[n] = 0
    while len(queue) != 0:
        pos = queue.popleft()
        for i in graph[pos]:
            if (i, pos) in history or (pos, i) in history:continue
            if dic[i] == -1:
                queue.append(i)
                dic[i] = dic[pos] + 1
                if i > N:
                    return True
    return False

history = set()
skip = set()

Q = int(input())
for _ in range(Q):
    X = int(input())
    history.add(li[X-1])
    cnt = 0
    for i in range(N):
        i += 1
        if i in skip: continue
        res = bfs(i)
        if res: cnt += 1
        else: skip.add(i)
    print(cnt)