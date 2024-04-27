from collections import deque

N = int(input())
A = list(map(int, input().split()))
A.reverse()

q = deque()
for _ in range(N):
    q.append(A.pop())
    while True:
        if len(q) <= 1:
            break
        if q[-1] != q[-2]:
            break
        else:
            a = q.pop()
            q.pop()
            q.append(a + 1)

print(len(q))
