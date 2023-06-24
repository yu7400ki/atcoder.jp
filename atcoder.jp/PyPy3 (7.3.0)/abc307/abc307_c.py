HA, WA = map(int, input().split())
A = [list(input()) for _ in range(HA)]
HB, WB = map(int, input().split())
B = [list(input()) for _ in range(HB)]
HX, WX = map(int, input().split())
X = [list(input()) for _ in range(HX)]

def trimming(grid, h, w):
    top = 0
    while all(grid[top][i] == "." for i in range(w)):
        top += 1
    bottom = h - 1
    while all(grid[bottom][i] == "." for i in range(w)):
        bottom -= 1
    left = 0
    while all(grid[i][left] == "." for i in range(top, bottom+1)):
        left += 1
    right = w - 1
    while all(grid[i][right] == "." for i in range(top, bottom+1)):
        right -= 1
    return [grid[i][left:right+1] for i in range(top, bottom+1)], bottom - top + 1, right - left + 1

def to_bit(grid, h, w, sy, sx):
    if h > sy or w > sx:
        raise ValueError("grid is too large")
    bit = 0
    for i in range(sy):
        for j in range(sx):
            if i >= h or j >= w:
                bit |= 0 << (i * sx + j)
            elif grid[i][j] == "#":
                bit |= 1 << (i * sx + j)
    return bit

A, HA, WA = trimming(A, HA, WA)
B, HB, WB = trimming(B, HB, WB)
X, HX, WX = trimming(X, HX, WX)

try:
    bitA = to_bit(A, HA, WA, HX, WX)
    bitB = to_bit(B, HB, WB, HX, WX)
    bitX = to_bit(X, HX, WX, HX, WX)
except ValueError:
    print("No")
    exit()

for dxa in range(WX - WA + 1):
    for dya in range(HX - HA + 1):
        for dxb in range(WX - WB + 1):
            for dyb in range(HX - HB + 1):
                a = bitA << (dya * WX + dxa)
                b = bitB << (dyb * WX + dxb)
                if a | b == bitX:
                    print("Yes")
                    exit()

print("No")
