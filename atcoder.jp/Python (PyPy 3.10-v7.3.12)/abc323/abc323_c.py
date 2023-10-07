N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [list(input()) for _ in range(N)]

def score(i: int) -> int:
    s = i
    for m in range(M):
        if S[i][m] == "o":
            s += A[m]
    return s

for i in range(N):
    my_score = score(i)
    max_score = 0
    for j in range(N):
        if i == j:
            continue
        max_score = max(max_score, score(j))
    unsolved = set(m for m in range(M) if S[i][m] == "x")
    rest = {m: a for m, a in enumerate(A) if m in unsolved}
    unsolved = sorted(unsolved, key=lambda x: rest[x], reverse=True)
    x = 0
    while my_score <= max_score:
        my_score += rest[unsolved[x]]
        x += 1
    print(x)
