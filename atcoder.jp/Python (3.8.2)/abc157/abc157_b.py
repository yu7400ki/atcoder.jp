A = [list(map(int,input().split())) for _ in range(3)]
N = int(input())

for i in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                A[i][j] = 0

idx = [(0,1,2), (3,4,5), (6,7,8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
for i in idx:
    if A[i[0]//3][i[0]%3] == A[i[1]//3][i[1]%3] == A[i[2]//3][i[2]%3] == 0:
        print('Yes')
        exit()

print('No')