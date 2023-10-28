from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A = deque(A)

ma = 0
lst = deque()

while A:
    if len(lst) == 0:
        lst.append(A.popleft())
    else:
        if A[0] - lst[0] >= M:
            l = lst.popleft()
        else:
            lst.append(A.popleft())
    ma = max(ma, len(lst))

print(ma)
