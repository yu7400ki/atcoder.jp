N, M = map(int,input().split())

for i in range(N):
    row = list(map(int,input().split()))
    if i != 0:
        if head != row[0] - 7:
            print('No')
            exit()
    head = row[0]
    for i in range(M-1):
        if row[i] == row[i+1]-1:
            pass
        else:
            print('No')
            exit()

print('Yes')