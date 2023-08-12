N = int(input())

roulette = [[] for _ in range(40)]
A_list = []

for i in range(N):
    C = int(input())
    A = list(map(int, input().split()))
    for a in A:
        roulette[a].append(i)
    A_list.append(A)

X = int(input())
roulette[X].sort(key=lambda x: len(A_list[x]))
if len(roulette[X]) == 0:
    print(0)
else:
    mi = roulette[X][0]
    ans = []
    for x in roulette[X]:
        if len(A_list[x]) == len(A_list[mi]):
            ans.append(x+1)
        else:
            break
    print(len(ans))
    print(*ans, sep=" ")
