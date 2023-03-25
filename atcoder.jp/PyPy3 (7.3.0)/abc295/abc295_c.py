N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 0
while len(A) > 1:
    if A[-1] == A[-2]:
        ans += 1
        A.pop()
        A.pop()
    else:
        A.pop()

print(ans)
