from collections import deque

N = int(input())
A = [list(input()) for _ in range(N)]

outside = deque()
y = 0
for x in range(N):
    outside.append(A[y][x])
for y in range(1, N):
    outside.append(A[y][x])
for x in range(x - 1, -1, -1):
    outside.append(A[y][x])
for y in range(y - 1, 0, -1):
    outside.append(A[y][x])
outside.appendleft(outside.pop())

y = 0
for x in range(N):
    A[y][x] = outside.popleft()
for y in range(1, N):
    A[y][x] = outside.popleft()
for x in range(x - 1, -1, -1):
    A[y][x] = outside.popleft()
for y in range(y - 1, 0, -1):
    A[y][x] = outside.popleft()

for a in A:
    print("".join(a))
