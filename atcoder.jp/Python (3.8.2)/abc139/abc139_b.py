A, B = map(int,input().split())

i = 0
cnt = 1
while True:
    if cnt >= B:
        print(i)
        break
    cnt += A - 1
    i += 1