N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

diff = [v - c for v, c in zip(V, C)]
ans = sum(d for d in diff if d > 0)

print(ans)
