from collections import deque

N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

ans = 0
for a, b in zip(A, B):
    ans += abs(a - b)

print(ans)
