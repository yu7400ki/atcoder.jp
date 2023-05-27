N, M, H, K = map(int, input().split())
S = list(input())
recover = set()
for _ in range(M):
    x, y = map(int, input().split())
    recover.add((x, y))
pos = (0, 0)

for s in S:
    H -= 1
    if H < 0:
        print("No")
        exit()
    if s == "R":
        pos = (pos[0] + 1, pos[1])
    elif s == "L":
        pos = (pos[0] - 1, pos[1])
    elif s == "U":
        pos = (pos[0], pos[1] + 1)
    elif s == "D":
        pos = (pos[0], pos[1] - 1)
    if pos in recover and H < K:
        H = K
        recover.discard(pos)
print("Yes")
