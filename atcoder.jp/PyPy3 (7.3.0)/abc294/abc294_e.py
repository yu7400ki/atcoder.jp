from collections import deque

L, N_1, N_2 = map(int, input().split())

V_1 = deque([None] * N_1)
V_2 = deque([None] * N_2)

for i in range(N_1):
    V_1[i] = list(map(int, input().split()))

for i in range(N_2):
    V_2[i] = list(map(int, input().split()))

ans = 0

while V_1 or V_2:
    a = V_1[0]
    b = V_2[0]

    if a[0] == b[0]:
        if a[1] > b[1]:
            ans += b[1]
        else:
            ans += a[1]

    if a[1] > b[1]:
        V_1[0][1] = a[1] - b[1]
        V_2.popleft()
    elif a[1] < b[1]:
        V_1.popleft()
        V_2[0][1] = b[1] - a[1]
    else:
        V_1.popleft()
        V_2.popleft()

print(ans)
