import bisect

N = int(input())
A = list(map(int, input().split()))

A_sorted = sorted(A)
acc = [0] * (N + 1)
for i in range(N):
    acc[i + 1] = acc[i] + A_sorted[i]

for i in range(N):
    a = A[i]
    # Aの要素のうち、A_iより大きな要素の和を求める
    idx = bisect.bisect_right(A_sorted, a)
    print(acc[N] - acc[idx])
