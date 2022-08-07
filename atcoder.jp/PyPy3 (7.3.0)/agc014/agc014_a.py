A, B, C = map(int, input().split())

history = set()
history.add((A, B, C))
cnt = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    A, B, C = B // 2 + C // 2, A // 2 + C // 2, A // 2 + B // 2
    cnt += 1
    if (A, B, C) in history:
        print(-1)
        exit()
    history.add((A, B, C))

print(cnt)