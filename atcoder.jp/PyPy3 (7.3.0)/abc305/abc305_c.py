from collections import Counter

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

h_count = [0] * H
w_count = [0] * W

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            h_count[i] += 1

for j in range(W):
    for i in range(H):
        if S[i][j] == "#":
            w_count[j] += 1

h_count_count = Counter(h_count)
w_count_count = Counter(w_count)

for k, v in h_count_count.items():
    if k == 0:
        continue
    if v == 1:
        h_unique = k

for k, v in w_count_count.items():
    if k == 0:
        continue
    if v == 1:
        w_unique = k

idx_y = h_count.index(h_unique) + 1
idx_x = w_count.index(w_unique) + 1

print(idx_y, idx_x)
