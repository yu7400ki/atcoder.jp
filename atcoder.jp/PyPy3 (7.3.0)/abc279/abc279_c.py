H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

Sh_cnt = [0] * H
Th_cnt = [0] * H
Sv_cnt = [0] * W
Tv_cnt = [0] * W

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            Sh_cnt[i] += 1
        if T[i][j] == "#":
            Th_cnt[i] += 1

for i in range(W):
    for j in range(H):
        if S[j][i] == "#":
            Sv_cnt[i] += 1
        if T[j][i] == "#":
            Tv_cnt[i] += 1

Sh_cnt.sort()
Th_cnt.sort()
Sv_cnt.sort()
Sv_cnt.sort()

if Sh_cnt == Th_cnt and Sv_cnt == Tv_cnt:
    print("Yes")
else:
    print("No")
