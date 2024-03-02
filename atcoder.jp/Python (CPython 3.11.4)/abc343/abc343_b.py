N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if A[i][j]:
            print(j + 1, end=' ')
    print()
