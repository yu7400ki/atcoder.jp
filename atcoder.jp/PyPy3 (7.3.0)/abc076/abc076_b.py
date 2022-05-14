n = int(input())
k = int(input())

now = 1
for _ in range(n):
    now = min(now * 2, now + k)
print(now)