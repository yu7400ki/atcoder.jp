N, W = map(int, input().split())

water = [0] * (2 * 10 ** 5 + 2)

for _ in range(N):
    S, T, P = map(int, input().split())
    water[S] += P
    water[T] -= P

for i in range(2 * 10 ** 5 + 1):
    water[i+1] += water[i]

if all(w <= W for w in water):
    print("Yes")
else:
    print("No")
