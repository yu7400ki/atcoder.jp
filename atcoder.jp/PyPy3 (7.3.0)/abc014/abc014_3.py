n = int(input())

count = [0] * (10**6+2)

for _ in range(n):
    a, b = map(int, input().split())
    count[a] += 1
    count[b+1] -= 1

for i in range(1, 10**6+1):
    count[i] += count[i-1]

print(max(count))
