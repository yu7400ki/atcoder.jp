from collections import deque
from functools import reduce

H, W = map(int, input().split())
A = deque([deque(input()) for _ in range(H)])
B = deque([deque(input()) for _ in range(H)])


for _ in range(H):
    candidates = [set() for _ in range(H)]
    A.appendleft(A.pop())
    for i in range(H):
        for j in range(W):
            a = A[i].pop()
            A[i].appendleft(a)
            if A[i] == B[i]:
                candidates[i].add(j)
    res = reduce(lambda x, y: x & y, candidates)
    if len(res) > 0:
        print("Yes")
        break
else:
    print("No")
