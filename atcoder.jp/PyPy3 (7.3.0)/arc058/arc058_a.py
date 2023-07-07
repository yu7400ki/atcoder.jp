N, K = map(int, input().split())
D = set(list(input()))

for i in range(1 << 31):
    if set(list(str(N + i))) & D == set():
        print(N + i)
        exit()
