H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
color = [i + 1 for i in range(N) for _ in range(a[i])]

for i in range(H):
    if i % 2 == 0:
        print(*color[i * W:(i + 1) * W])
    else:
        print(*color[i * W:(i + 1) * W][::-1])
