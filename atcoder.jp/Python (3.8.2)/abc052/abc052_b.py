input()
S = input()

ma = 0
x = 0
for s in S:
    if s == 'I':
        x += 1
    elif s == 'D':
        x -= 1
    ma = max(ma, x)

print(ma)