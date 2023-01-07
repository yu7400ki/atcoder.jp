N = int(input())

ans = 0

if N % 2 == 1:
    print(ans)
    exit()

N //= 2
while N:
    ans += N // 5
    N //= 5

print(ans)
