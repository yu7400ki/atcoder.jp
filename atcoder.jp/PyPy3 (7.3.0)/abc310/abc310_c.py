N = int(input())
S = [input() for _ in range(N)]

count = {}

for s in S:
    s = min(s, s[::-1])
    count[s] = count.get(s, 0) + 1

print(len(count))
