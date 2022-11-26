H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

S_cnt = []
T_cnt = []

for i in range(W):
    s = 0
    t = 0
    for j in range(H):
        if S[j][i] == "#":
            s += 1
        if T[j][i] == "#":
            t += 1
    S_cnt.append(s)
    T_cnt.append(t)

S_cnt.sort()
T_cnt.sort()

if S_cnt == T_cnt:
    print("Yes")
else:
    print("No")
