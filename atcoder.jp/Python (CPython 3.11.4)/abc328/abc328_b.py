N = int(input())
D = list(map(int, input().split()))

ans = 0
for i, d in enumerate(D):
    for j in range(d):
        s = str(i + 1) + str(j + 1)
        ans += len(set(s)) == 1

print(ans)
