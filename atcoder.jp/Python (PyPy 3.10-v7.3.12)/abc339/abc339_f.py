from collections import Counter

N = int(input())
A = [int(input()) for _ in range(N)]

cnt = Counter(A)

ans = 0
for i in range(N):
    for j in range(i, N):
        t = A[i] * A[j]
        ans += cnt[t] * 2 if i != j else cnt[t]

print(ans)
