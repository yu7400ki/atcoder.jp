N, H = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

a_max = max(A)
B.sort(reverse=True)
b_acc = [0] * (N + 1)
for i in range(N):
    b_acc[i + 1] = b_acc[i] + B[i]

ans = 1 << 60
for i in range(N + 1):
    b = b_acc[i]
    rest = H - b
    if rest > 0:
        tmp = i + (H - b + a_max - 1) // a_max
    else:
        tmp = i
    ans = min(ans, tmp)

print(ans)
