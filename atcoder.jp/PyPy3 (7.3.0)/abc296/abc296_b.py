S = [list(input()) for _ in range(8)]

alf = "abcdefgh"

for y in range(8):
    for x in range(8):
        if S[y][x] == "*":
            ans = f"{alf[x]}{8 - y}"
            break

print(ans)
