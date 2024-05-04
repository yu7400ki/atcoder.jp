from collections import deque

N = int(input())
A = deque()
B = deque()
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b - a)

print(sum(A) + max(B))
