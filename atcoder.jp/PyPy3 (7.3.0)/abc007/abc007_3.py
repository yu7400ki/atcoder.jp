from collections import deque

R, C = map(int,input().split())
sy, sx = map(int,input().split())
gy, gx = map(int,input().split())
c = [list(input()) for _ in range(R)]
memo = [[-1] * C for _ in range(R)]
sy -= 1; sx -= 1; gy -= 1; gx -= 1
memo[sy][sx] = 0

queue = deque([(sy,sx)])
while len(queue) != 0:
    pos = queue.popleft()
    idx = [(pos[0]+1,pos[1]), (pos[0],pos[1]+1), (pos[0]-1,pos[1]), (pos[0],pos[1]-1)]
    for i in idx:
        y = i[0]; x = i[1]
        if c[y][x] == '.':
            memo[y][x] = memo[pos[0]][pos[1]] + 1
            if y == gy and x == gx:
                print(memo[y][x])
                exit()
            c[y][x] = '#'
            queue.append((y,x))