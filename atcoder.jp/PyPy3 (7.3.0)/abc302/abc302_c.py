from itertools import permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]

def diff_cnt(s1, s2):
    cnt = 0
    for i in range(M):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt


for p in permutations(S, N):
    for i in range(N - 1):
        if diff_cnt(p[i], p[i + 1]) > 1:
            break
    else:
        print("Yes")
        exit()

print("No")
