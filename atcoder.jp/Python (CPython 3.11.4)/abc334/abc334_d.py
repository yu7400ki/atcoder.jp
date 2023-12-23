from bisect import bisect_right

N, Q = map(int, input().split())
R = list(map(int, input().split()))
R.sort()

acc = [0] * (N + 1)
for i in range(N):
    acc[i + 1] = acc[i] + R[i]

for _ in range(Q):
    x = int(input())
    i = bisect_right(acc, x)
    print(i - 1)
