import numpy as np
from sys import stdin

N, M = map(int, stdin.readline().split())
A = np.array([list(map(int, stdin.readline().split())) for _ in range(N)], dtype=np.int16)

ans = 0
for i in range(N):
    matching_counts = np.sum(A[i] == A[i + 1 :], axis=1)
    ans += np.count_nonzero(matching_counts % 2 == 1)

print(ans)
