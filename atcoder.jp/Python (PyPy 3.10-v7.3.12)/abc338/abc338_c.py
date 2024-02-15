N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

inf = 1 << 60
ans = 0
for i in range(10**6 + 1):
    rest = [q - a * i for q, a in zip(Q, A)]
    if any([r < 0 for r in rest]):
        break
    j = min([r // b if b > 0 else inf for r, b in zip(rest, B)])
    ans = max(ans, i + j)

print(ans)
