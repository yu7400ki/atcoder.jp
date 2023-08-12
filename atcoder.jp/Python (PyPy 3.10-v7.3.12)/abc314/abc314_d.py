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

for i in range(len(history)):
    if history[i][0] > last_operation:
        break
    x, c = history[i][1:]
    S[x-1] = c

if is_upper:
    S = list(map(lambda x: x.upper(), S))
elif is_lower:
    S = list(map(lambda x: x.lower(), S))

for i in range(len(history)):
    if history[i][0] < last_operation:
        continue
    x, c = history[i][1:]
    S[x-1] = c

print("".join(S))
