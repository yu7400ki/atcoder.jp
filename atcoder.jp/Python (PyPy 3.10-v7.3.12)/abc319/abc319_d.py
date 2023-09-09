N, M = map(int, input().split())
L = list(map(int, input().split()))

width = max(sum(L) // M, max(L))
ng = width - 1
ok = width + 1000

while ok - ng > 1:
    width = (ok + ng) // 2
    row = 0
    col = 1
    for l in L:
        if row + l <= width:
            if row + l == width:
                row += l
            else:
                row += l + 1
        else:
            row = l + 1
            col += 1
    if col <= M:
        ok = width
    else:
        ng = width

print(ok)
