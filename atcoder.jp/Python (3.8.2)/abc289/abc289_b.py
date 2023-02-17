N, M = map(int, input().split())
A = set(map(int, input().split()))

ans = []
pos = 1

while pos <= N:
    tmp = [pos]
    while pos in A:
        pos += 1
        tmp.append(pos)
    pos += 1
    ans.extend(tmp[::-1])

print(*ans)
