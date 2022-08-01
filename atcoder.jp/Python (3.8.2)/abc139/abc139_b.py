A, B = map(int,input().split())

i = 1
while True:
    if A * i - (i-1) >= B:
        print(i)
        break
    i += 1