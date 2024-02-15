N = int(input())

M = len(bin(N)) - 2
print(M)

for i in range(M):
    l = []
    for j in range(N):
        if (j >> i) & 1:
            l.append(j + 1)
    print(len(l), *l)

S = int(input()[::-1], 2)
print(S + 1)
