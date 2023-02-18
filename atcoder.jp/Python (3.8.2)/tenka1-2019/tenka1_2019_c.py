N = int(input())
S = list(input())

black = 0
white = S.count(".")

ans = white

for i in range(N):
    if S[i] == "#":
        black += 1
    else:
        white -= 1
    ans = min(ans, black + white)

print(ans)
