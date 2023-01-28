N = int(input())
S = [input() for _ in range(N)]

f = S.count('For')
a = S.count('Against')

if f > a:
    print("Yes")
else:
    print("No")
