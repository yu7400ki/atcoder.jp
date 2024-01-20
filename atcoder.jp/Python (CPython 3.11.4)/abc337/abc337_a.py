N = int(input())
x = 0
y = 0
for _ in range(N):
    X, Y = map(int, input().split())
    x += X
    y += Y
if x > y:
    print("Takahashi")
elif x < y:
    print("Aoki")
else:
    print("Draw")
