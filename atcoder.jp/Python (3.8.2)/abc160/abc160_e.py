X, Y, A, B, C = map(int, input().split())
P = sorted(list(map(int, input().split())), reverse=True)
Q = sorted(list(map(int, input().split())), reverse=True)
R = sorted(list(map(int, input().split())), reverse=True)

P = P[:X]
Q = Q[:Y]

candidates = P + Q + R
candidates.sort(reverse=True)
ans = sum(candidates[:X+Y])

print(ans)
