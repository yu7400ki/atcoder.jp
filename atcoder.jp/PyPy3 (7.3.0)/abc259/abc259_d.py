from collections import defaultdict, deque

N = int(input())
sx,sy,tx,ty = map(int,input().split())
xyr = [list(map(int,input().split())) for _ in range(N)]

graph = defaultdict(list)

def bfs(n):
    dic = defaultdict(lambda : -1)
    queue = deque()
    queue.append(n)
    dic[n] = 0
    while len(queue) != 0:
        pos = queue.popleft()
        for i in graph[pos]:
            if dic[i] == -1:
                queue.append(i)
                dic[i] = dic[pos] + 1
    return dic

def is_collision(x1, y1, r1, x2, y2, r2):
    return ((x1-x2)**2 + (y1-y2)**2 >= (r1-r2)**2) and ((x1-x2)**2 + (y1-y2)**2 <= (r1+r2)**2)

start = -1
end = -1

for i in range(N):
    if (sx - xyr[i][0])**2 + (sy - xyr[i][1])**2 == xyr[i][2]**2: start = i
    if (tx - xyr[i][0])**2 + (ty - xyr[i][1])**2 == xyr[i][2]**2: end = i
    for j in range(i+1, N):
        if is_collision(xyr[i][0], xyr[i][1], xyr[i][2], xyr[j][0], xyr[j][1], xyr[j][2]):
            graph[i].append(j)
            graph[j].append(i)

if start == -1 or end == -1:
    print('No')
    exit()
elif start == end:
    print('Yes')
    exit()
else:
    res = bfs(start)
    print('Yes' if res[end] != -1 else 'No')