N = int(input())
A = [list(input()) for i in range(N)]

flag = 0
for i in range(N):
    for j in range(i+1, N):
        if A[i][j] == 'W':
            if A[j][i] != 'L':
                flag = 1
        elif A[i][j] == 'L':
            if A[j][i] != 'W':
                flag = 1
        else:
            if A[i][j] != A[j][i]:
                flag = 1
if flag == 1:
    print('incorrect')
else:
    print('correct')