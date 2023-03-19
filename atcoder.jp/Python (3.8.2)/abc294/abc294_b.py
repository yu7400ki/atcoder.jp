from string import ascii_uppercase

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = []

for a in A:
    res = map(lambda x: "." if x == 0 else ascii_uppercase[x - 1], a)
    ans.append(res)

for a in ans:
    print(*a, sep='')
