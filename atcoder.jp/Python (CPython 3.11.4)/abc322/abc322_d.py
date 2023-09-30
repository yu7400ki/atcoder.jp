P = [list(input()) for _ in range(4)]
Q = [list(input()) for _ in range(4)]
R = [list(input()) for _ in range(4)]


def trimming(grid):
    h = len(grid)
    w = len(grid[0])
    top = 0
    while all(grid[top][i] == "." for i in range(w)):
        top += 1
    bottom = h - 1
    while all(grid[bottom][i] == "." for i in range(w)):
        bottom -= 1
    left = 0
    while all(grid[i][left] == "." for i in range(top, bottom + 1)):
        left += 1
    right = w - 1
    while all(grid[i][right] == "." for i in range(top, bottom + 1)):
        right -= 1
    return (
        [grid[i][left : right + 1] for i in range(top, bottom + 1)],
        bottom - top + 1,
        right - left + 1,
    )


def to_bit(grid, sy, sx):
    h = len(grid)
    w = len(grid[0])
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


def count_one(bit):
    cnt = 0
    while bit > 0:
        cnt += bit & 1
        bit >>= 1
    return cnt


def rotate(grid):
    h = len(grid)
    w = len(grid[0])
    return [[grid[h - 1 - j][i] for j in range(h)] for i in range(w)]


if (
    count_one(to_bit(P, 4, 4)) + count_one(to_bit(Q, 4, 4)) + count_one(to_bit(R, 4, 4))
    != 16
):
    print("No")
    exit()

for i in range(4):
    P = rotate(P)
    trimmed_P, HP, WP = trimming(P)
    P_bit = to_bit(trimmed_P, 4, 4)
    for j in range(4):
        Q = rotate(Q)
        trimmed_Q, HQ, WQ = trimming(Q)
        Q_bit = to_bit(trimmed_Q, 4, 4)
        for k in range(4):
            R = rotate(R)
            trimmed_R, HR, WR = trimming(R)
            R_bit = to_bit(trimmed_R, 4, 4)
            for dxp in range(4 - WP + 1):
                for dyp in range(4 - HP + 1):
                    for dxr in range(4 - WR + 1):
                        for dyr in range(4 - HR + 1):
                            for dxq in range(4 - WQ + 1):
                                for dyq in range(4 - HQ + 1):
                                    p = P_bit << (dyp * 4 + dxp)
                                    q = Q_bit << (dyq * 4 + dxq)
                                    r = R_bit << (dyr * 4 + dxr)
                                    if p | q | r == 0xFFFF:
                                        print("Yes")
                                        exit()

print("No")
