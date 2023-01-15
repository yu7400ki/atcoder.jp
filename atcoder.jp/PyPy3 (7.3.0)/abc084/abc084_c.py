N = int(input())
CSF = [tuple(map(int, input().split())) for _ in range(N-1)]


for pos in range(N):
    t = 0

    for c, s, f in CSF[pos:]:
        if t < s:
            t = s
        elif t % f != 0:
            t += f - t % f
        t += c

    print(t)
