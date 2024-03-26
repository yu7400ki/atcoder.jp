N, K = map(int, input().split())
A = list(map(int, input().split()))

s = K * (K + 1) // 2
s -= sum(set(a for a in A if a <= K))

print(s)
