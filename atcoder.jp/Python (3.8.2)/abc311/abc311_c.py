N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))

hare = tortoise = 0
while True:
    hare = A[A[hare]]
    tortoise = A[tortoise]
    if hare == tortoise:
        break

ans = [tortoise]
tortoise = A[tortoise]
while tortoise != ans[0]:
    ans.append(tortoise)
    tortoise = A[tortoise]

print(len(ans))
print(*map(lambda x: x + 1, ans))
