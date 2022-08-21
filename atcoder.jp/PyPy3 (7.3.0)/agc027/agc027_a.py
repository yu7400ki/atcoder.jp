N, x = map(int,input().split())
A = list(map(int,input().split()))

A.sort()

ans = 0
for a in A:
    if a <= x:
        x -= a
        ans += 1
    else:
        break

if x > 0 and ans > 0:
    ans -= 1

print(ans)