def ceil(x, y):
    return (x + y - 1) // y

N, H = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

wield = max(A)
throw = []
for b in B:
    if b > wield:
        throw.append(b)

ans = len(throw)
s = sum(throw)
H -= s
ans += ceil(H, wield)

print(ans)
