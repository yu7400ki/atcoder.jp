N = int(input())
S = list(input())

pos_x = 0
pos_y = 0
pos = set()
pos.add((pos_x, pos_y))
flag = False

for s in S:
    match s:
        case "L":
            pos_x -= 1
        case "R":
            pos_x += 1
        case "U":
            pos_y += 1
        case "D":
            pos_y -= 1
        case _:
            raise NotImplementedError()
    now = (pos_x, pos_y)
    if now in pos:
        flag = True
        break
    else:
        pos.add(now)

if flag:
    print("Yes")
else:
    print("No")
