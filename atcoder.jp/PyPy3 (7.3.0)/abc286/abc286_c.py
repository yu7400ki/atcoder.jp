from collections import deque

N, A, B = map(int, input().split())
S = deque(input())

ans = float("inf")

for i in range(N):
    temp = i * A
    for j in range(N // 2):
        if S[j] != S[-j - 1]:
            temp += B
    ans = min(ans, temp)
    s = S.popleft()
    S.append(s)

print(ans)
