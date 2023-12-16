N = int(input())

event = []
for _ in range(N):
    t, x = map(int, input().split())
    event.append((t, x - 1))
event.reverse()

enemy = [0] * N
action = []
k = 0
k_max = 0
for t, x in event:
    if t == 1:
        if enemy[x] == 0:
            action.append(0)
        else:
            enemy[x] -= 1
            action.append(1)
            k -= 1
    elif t == 2:
        enemy[x] += 1
        k += 1
        k_max = max(k_max, k)

if any(enemy):
    print(-1)
    exit()

action.reverse()
print(k_max)
print(*action)
