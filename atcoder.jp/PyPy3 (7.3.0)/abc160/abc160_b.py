X = int(input())

ans = 0
for i in [500,5]:
    ans += X // i * (1000 if i == 500 else 5)
    X %= i

print(ans)