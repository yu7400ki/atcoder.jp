N = int(input())
v = list(map(int, input().split()))

from collections import deque
v = deque(sorted(v))

while len(v) > 1:
    v[1] = (v[0] + v[1]) / 2
    v.popleft()

print(v[0])