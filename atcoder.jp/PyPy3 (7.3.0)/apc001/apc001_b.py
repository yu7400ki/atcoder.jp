N = int(input())
A = map(int, input().split())
B = map(int, input().split())

res = 0

for a, b in zip(A, B):
    if a > b:
        res -= a - b
    else:
        res += (b - a) // 2

print('Yes' if res >= 0 else 'No')
