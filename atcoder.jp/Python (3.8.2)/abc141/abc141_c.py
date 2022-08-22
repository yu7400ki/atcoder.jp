N, K, Q = map(int,input().split())

score = [0] * N

for _ in range(Q):
    A = int(input())
    score[A-1] += 1

mi = sum(score)
for s in score:
    if K - mi + s > 0:
        print('Yes')
    else:
        print('No')