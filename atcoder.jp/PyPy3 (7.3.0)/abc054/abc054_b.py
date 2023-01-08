N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]

for i in range(N - M + 1):
    for j in range(N - M + 1):
        for y in range(M):
            for x in range(M):
                if A[i + y][j + x] != B[y][x]:
                    break
            else:
                print('Yes')
                exit()

print('No')
