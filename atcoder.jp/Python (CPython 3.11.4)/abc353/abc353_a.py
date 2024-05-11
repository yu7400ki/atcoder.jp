N = int(input())
H = list(map(int, input().split()))

h = H[0]
ans = -1
for i in range(N - 1, 0, -1):
    if h < H[i]:
        ans = i + 1

print(ans)
