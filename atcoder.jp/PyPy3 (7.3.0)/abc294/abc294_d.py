from collections import deque

N, Q = map(int, input().split())

queue = deque(range(1, N + 1))
called = deque()
gone = set()
ans = []

for i in range(Q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        call = queue.popleft()
        called.append(call)
    elif event[0] == 2:
        x = event[1]
        gone.add(x)
    elif event[0] == 3:
        while called[0] in gone:
            called.popleft()
        ans.append(called[0])

for a in ans:
    print(a)
