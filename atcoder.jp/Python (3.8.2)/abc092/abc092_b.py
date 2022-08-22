N = int(input())
D, X = map(int,input().split())


for i in range(N):
    A = int(input())
    for j in range(D):
        day = j * A + 1
        if day > D: break
        X += 1


print(X)