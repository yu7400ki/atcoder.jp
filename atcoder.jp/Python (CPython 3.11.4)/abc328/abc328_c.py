N, Q = map(int, input().split())
S = list(input())

arr = [0] * N
for i in range(N - 1):
    if S[i] == S[i + 1]:
        arr[i] = 1

acc = [0] * (N + 1)
for i in range(N):
    acc[i + 1] = acc[i] + arr[i]

for _ in range(Q):
    l, r = map(int, input().split())
    print(acc[r - 1] - acc[l - 1])
