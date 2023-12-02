N, S, M, L = map(int, input().split())

ans = float("inf")
for i in range(100):
    for j in range(100):
        for k in range(100):
            if i * 6 + j * 8 + k * 12 >= N:
                ans = min(ans, i * S + j * M + k * L)

print(ans)
