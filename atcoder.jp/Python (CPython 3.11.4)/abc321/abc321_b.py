N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(101):
    score = A + [i]
    score.sort()
    res = sum(score[1:N-1])
    if res >= X:
        print(i)
        break
else:
    print(-1)
