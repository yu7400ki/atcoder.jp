N = int(input())
A = set(map(int, input().split()))

ma = max(A)
A.remove(ma)
pair = min(A, key = lambda x: abs(x - ma / 2))

print(ma, pair)
