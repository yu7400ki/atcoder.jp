A, B = map(int,input().split())

for i in range(200):
    if A * (i+1) - i >= B:
        print(i+1)
        break