N = int(input())
A = list(map(int, input().split()))

b = [0] * N

for i in range(N - 1, -1 , -1):
    b[i] = (sum(b[i::i+1]) + A[i]) % 2

print(b.count(1))
print(*[i + 1 for i in range(N) if b[i]])
