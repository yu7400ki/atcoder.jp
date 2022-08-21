H, W = map(int,input().split())
G = [list(input()) for _ in range(H)]

pos = [0, 0]
visited = set()

while True:
    if (pos[0], pos[1]) in visited:
        print(-1)
        exit()
    visited.add((pos[0], pos[1]))
    s = G[pos[0]][pos[1]]
    if s == 'U':
        if pos[0] != 0:
            pos[0] -= 1
        else:
            print(pos[0] + 1, pos[1] + 1)
            exit()
    elif s == 'D':
        if pos[0] != H-1:
            pos[0] += 1
        else:
            print(pos[0] + 1, pos[1] + 1)
            exit()
    elif s == 'L':
        if pos[1] != 0:
            pos[1] -= 1
        else:
            print(pos[0] + 1, pos[1] + 1)
            exit()
    elif s == 'R':
        if pos[1] != W-1:
            pos[1] += 1
        else:
            print(pos[0] + 1, pos[1] + 1)
            exit()
            