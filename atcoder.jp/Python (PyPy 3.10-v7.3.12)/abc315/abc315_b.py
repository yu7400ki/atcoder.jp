M = int(input())
D = list(map(int, input().split()))

def ceil(a, b):
    return (a + b - 1) // b

d_sum = sum(D)
d_mid = ceil(d_sum, 2)

for i, d in enumerate(D):
    d_sum -= d
    if d_sum < d_mid:
        print(i + 1, d - d_mid + d_sum + 1)
        break
