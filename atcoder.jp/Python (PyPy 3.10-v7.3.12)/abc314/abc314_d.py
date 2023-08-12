N = int(input())
S = list(input())
Q = int(input())

is_upper = False
is_lower = False
last_operation = None
history = []

for i in range(Q):
    t, x, c = input().split()
    t, x = int(t), int(x)
    match t:
        case 1:
            history.append((i, x, c))
        case 2:
            is_lower = True
            is_upper = False
            last_operation = i
        case 3:
            is_lower = False
            is_upper = True
            last_operation = i
        case _:
            continue

if last_operation is None:
    for i, x, c in history:
        S[x-1] = c
    print("".join(S))
    exit()

for i, x, c in history:
    if i > last_operation:
        break
    S[x-1] = c

if is_upper:
    S = list(map(lambda x: x.upper(), S))
elif is_lower:
    S = list(map(lambda x: x.lower(), S))

for i, x, c in history:
    if i < last_operation:
        continue
    S[x-1] = c

print("".join(S))
