N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    print(S[N - i - 1])
