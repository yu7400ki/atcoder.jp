N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB_sorted = sorted(AB, key=lambda x: x[0])

acc = [0] * (N + 1)
for i, (a_i, b_i) in enumerate(AB_sorted):
    acc[0] += b_i
    acc[i + 1] -= b_i

for i in range(N):
    acc[i + 1] += acc[i]

for i in range(N):
    if acc[i] <= K:
        if i == 0:
            print(1)
        else:
            print(AB_sorted[i - 1][0] + 1)
        break
