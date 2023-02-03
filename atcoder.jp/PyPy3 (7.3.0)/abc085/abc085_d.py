N, H = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

a_max = max(A)
B.sort()

ans = 0
while B and B[-1] > a_max and H > 0:
    H -= B.pop()
    ans += 1

if H > 0:
    ans += (H + a_max - 1) // a_max

print(ans)
