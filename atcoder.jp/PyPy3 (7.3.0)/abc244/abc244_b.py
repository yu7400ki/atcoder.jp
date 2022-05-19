N = int(input())
T = list(input())

pos = [0,0]
go = [1,0]
for i in range(N):
    if T[i] == 'S':
        pos[0] += go[0]
        pos[1] += go[1]
    else:
        go[0], go[1] = go[1], -1 * go[0]
print(*pos)