N, x = map(int,input().split())
A = list(map(int,input().split()))

A.sort()

ans = 0
cnt = 0
for a in A:
    if a <= x:
        x -= a
        ans += 1
        cnt += 1
    else:
        break

if x > 0 and cnt == N:
    ans -= 1

print(ans)