N, L, R = map(int, input().split())
A = list(map(int, input().split()))

def solve(a):
  if L <= a <= R:
    return a
  else:
    return min([L, R], key=lambda x: abs(x - a))

ans = [solve(a) for a in A]
print(*ans)
