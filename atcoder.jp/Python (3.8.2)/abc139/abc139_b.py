A, B = map(int,input().split())

i = 0
while True:
    if A * (i+1) - i >= B:
        print(i+1)
        break
    i += 1