S = list(input().split())
T = list(input().split())

cnt = 0
while True:
    T[0], T[1] = T[1], T[0]
    cnt += 1
    if S == T:
        break
    T[1], T[2] = T[2], T[1]
    cnt += 1
    if S == T:
        break

print('Yes' if cnt % 2 == 0 else 'No')