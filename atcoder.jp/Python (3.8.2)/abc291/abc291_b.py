from statistics import mean

N = int(input())
X = sorted(map(int, input().split()))

X = X[N:4 * N]

print(mean(X))
