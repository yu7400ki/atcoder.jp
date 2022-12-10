N, T = map(int, input().split())
A = list(map(int, input().split()))

A_sum = sum(A)
T %= A_sum

res = [0] * (len(A) + 1)
for i, n in enumerate(A):
    res[i+1] = res[i] + n

for i in range(len(A)):
    if res[i+1] > T:
        print(i+1, T - res[i])
        break
