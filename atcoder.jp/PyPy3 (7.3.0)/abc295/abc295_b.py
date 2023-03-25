R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

for y in range(R):
    for x in range(C):
        if B[y][x] == "#" or B[y][x] == ".":
            continue
        i = int(B[y][x])
        B[y][x] = "."
        for y2 in range(R):
            for x2 in range(C):
                if manhattan_distance(x, y, x2, y2) <= i:
                    if B[y2][x2] == "#":
                        B[y2][x2] = "."

for y in range(R):
    print("".join(B[y]))
