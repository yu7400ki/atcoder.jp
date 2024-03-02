N = int(input())

ans = 1
for i in range(N):
    k = i ** 3
    if k > N:
        break
    if str(k) == str(k)[::-1]:
        ans = k

print(ans)
