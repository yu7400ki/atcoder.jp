from collections import deque

N, M = map(int, input().split())
A = deque(map(int, input().split()))
B = deque(map(int, input().split()))

ans_A = []
ans_B = []

i = 1
while A and B:
    if A[0] < B[0]:
        ans_A.append(i)
        A.popleft()
    else:
        ans_B.append(i)
        B.popleft()
    i += 1

while A:
    ans_A.append(i)
    A.popleft()
    i += 1

while B:
    ans_B.append(i)
    B.popleft()
    i += 1

print(*ans_A, sep=' ')
print(*ans_B, sep=' ')
