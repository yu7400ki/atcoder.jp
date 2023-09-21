N, M = map(int, input().split())
A = [list(map(lambda c: 0 if c == "G" else 1 if c == "C" else 2, list(input()))) for _ in range(2 * N)]

win = [0] * (2 * N)
ranking = list(range(2 * N))

for i in range(M):
    for k in range(N):
        l = ranking[2 * k]
        r = ranking[2 * k + 1]
        d = (A[r][i] - A[l][i]) % 3
        if d == 1:
            win[l] += 1
        elif d == 2:
            win[r] += 1
    tmp = [[] for _ in range(M + 1)]
    for i, w in enumerate(win):
        tmp[M - w].append(i)
    ranking = [x for t in tmp for x in t]

for r in ranking:
    print(r + 1)
