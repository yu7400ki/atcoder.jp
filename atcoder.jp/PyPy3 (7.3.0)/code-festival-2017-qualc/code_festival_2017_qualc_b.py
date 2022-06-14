N = int(input())
A = list(map(int,input().split()))

ans = 3**N
cnt = 1
for a in A:
    if a % 2 == 0:
        cnt *= 2

ans -= cnt
print(ans)