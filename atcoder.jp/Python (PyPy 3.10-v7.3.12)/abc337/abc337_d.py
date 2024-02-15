H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]

ans = float("inf")
for _ in range(2):
    for y in range(H):
        window = S[y][:K]
        cnt = {
            "o": window.count("o"),
            "x": window.count("x"),
            ".": window.count("."),
        }
        if cnt["o"] + cnt["."] == K:
            ans = min(ans, cnt["."])
        for x in range(W - K):
            cnt[S[y][x]] -= 1
            cnt[S[y][x + K]] += 1
            if cnt["o"] + cnt["."] == K:
                ans = min(ans, cnt["."])
    S = [list(x) for x in zip(*S)]
    H, W = W, H

print(ans if ans != float("inf") else -1)
