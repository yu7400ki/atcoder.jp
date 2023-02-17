N, M = map(int, input().split())
S = []
for _ in range(M):
    input()
    S.append(set(map(int, input().split())))

ans = 0

for i in range(1, 1 << M):
    flag = [False] * N
    for x in range(1, N + 1):
        for j in range(M):
            if i & (1 << j) == 0:
                continue
            if x in S[j]:
                flag[x - 1] = True
    ans += all(flag)

print(ans)
