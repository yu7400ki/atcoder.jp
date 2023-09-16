from itertools import permutations

M = int(input())
S1 = list(map(int, list(input())))
S2 = list(map(int, list(input())))
S3 = list(map(int, list(input())))

S1_idx = [[] for _ in range(10)]
S2_idx = [[] for _ in range(10)]
S3_idx = [[] for _ in range(10)]

for i in range(M):
    S1_idx[S1[i]].append(i)
    S2_idx[S2[i]].append(i)
    S3_idx[S3[i]].append(i)

idx = [S1_idx, S2_idx, S3_idx]

ans = float("inf")
for i in range(10):
    if len(idx[0][i]) == 0 or len(idx[1][i]) == 0 or len(idx[2][i]) == 0:
        continue
    for p in permutations(range(3)):
        res = [idx[p[0]][i][0]]
        j = 0
        target = idx[p[1]][i]
        num = len(idx[p[1]][i])
        while True:
            time = target[j % num] + (j // num * M)
            if time in res:
                j += 1
            else:
                res.append(time)
                break
        j = 0
        target = idx[p[2]][i]
        num = len(idx[p[2]][i])
        while True:
            time = target[j % num] + (j // num * M)
            if time in res:
                j += 1
            else:
                res.append(time)
                break
        ans = min(ans, max(res))

if ans == float("inf"):
    print(-1)
else:
    print(ans)
