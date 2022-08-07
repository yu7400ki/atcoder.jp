N, K = map(int,input().split())

rev = N
while True:
    if N > K:
        N = N - N//K * K
    else:
        N = K - N
    if N >= rev:
        print(rev)
        exit()
    rev = N