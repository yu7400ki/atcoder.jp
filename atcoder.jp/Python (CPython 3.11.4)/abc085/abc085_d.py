def ceil(x, y):
    return (x + y - 1) // y

N, H = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b
B.sort()

wield = max(A)
s = 0
throw = []
for b in B:
    if s >= H:
        break
    if b > wield:
        s += b
        throw.append(b)

ans = len(throw)
s = sum(throw)
H -= s

if H > 0:
    ans += ceil(H, wield)

print(ans)
