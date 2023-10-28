from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A = deque(A)

ma = 0
lst = deque()

lst.append(A.popleft())
cu = 1

while A:
    if A[0] - lst[0] >= M:
        l = lst.popleft()
        cu -= 1
    else:
        cu += 1
        lst.append(A.popleft())
    if len(lst) == 0:
        cu += 1
        lst.append(A.popleft())
    ma = max(ma, cu)

print(ma)
