N, M, P = map(int, input().split())

ans = 0

i = 0
while True:
    if M + P * i <= N:
        ans += 1
    else:
        break
    i += 1

print(ans)
