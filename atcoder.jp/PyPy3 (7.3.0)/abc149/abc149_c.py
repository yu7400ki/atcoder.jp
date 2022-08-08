X = int(input())

if X == 2:
    print(X)
    exit()

P = [2]
N = 3
while True:
    for p in P:
        if N ** 0.5 < p:
            P.append(N)
            if N > X:
                print(N)
                exit()
            break
        if N % p == 0:
            break
    N += 2