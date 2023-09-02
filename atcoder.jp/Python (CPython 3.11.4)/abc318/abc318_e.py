N = int(input())
A = list(map(int, input().split()))

idx = [-1] * (N + 1)
cnt = [0] * (N + 1)
ans = 0

for i in range(N):
    a = A[i]
    if idx[a] == -1:
        idx[a] = i
    else:
        ans += i - idx[a] - cnt[a] - 1
        cnt[a] += 1

print(ans)
