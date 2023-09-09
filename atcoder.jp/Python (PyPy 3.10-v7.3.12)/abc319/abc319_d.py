N, M = map(int, input().split())
L = list(map(int, input().split()))

width = sum(L) // M

while True:
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
    if col == M:
        break
    else:
        width += 1

print(width)
