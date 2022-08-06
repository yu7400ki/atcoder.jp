N = int(input())
P = list(map(int,input().split()))

N -= 2
cnt = 1
par = P[N]
while True:
    if par == 1:
        print(cnt)
        exit()
    par = P[par-2]
    cnt += 1