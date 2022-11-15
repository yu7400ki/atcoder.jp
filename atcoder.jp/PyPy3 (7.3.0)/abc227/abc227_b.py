N = int(input())
S = list(map(int, input().split()))

enum = set()

for a in range(1, 1000):
    for b in range(1, 1000):
        enum.add(4*a*b + 3*a + 3*b)


cnt = 0
for s in S:
    if s in enum:
        cnt += 1

print(N-cnt)
