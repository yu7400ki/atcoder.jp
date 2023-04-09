N, D = map(int, input().split())
T = list(map(int, input().split()))

for i in range(N - 1):
    d = T[i + 1] - T[i]
    if d <= D:
        print(T[i + 1])
        break
else:
    print(-1)
