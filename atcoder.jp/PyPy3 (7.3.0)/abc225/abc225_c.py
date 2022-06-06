N, M = map(int,input().split())

LIMIT  = 10**100

for i in range(N):
    row = list(map(int,input().split()))
    if i != 0:
        if head != row[0] - 7:
            print('No')
            exit()
    else:
        j = row[0] % 7
        if j == 0: j = 7
    head = row[0]
    if (head - j) // 7 + 1 > LIMIT:
        print('No')
        exit()
    for i in range(M-1):
        if row[i] == row[i+1]-1:
            pass
        else:
            print('No')
            exit()

print('Yes')