N, M = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        p1, c1, *f1 = P[i]
        p2, c2, *f2 = P[j]
        f1 = set(f1)
        f2 = set(f2)
        if p1 >= p2 and f2 >= f1 and (p1 > p2 or len(f2 - f1) > 0):
            print("Yes")
            exit()

print("No")
