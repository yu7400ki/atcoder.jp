from itertools import combinations

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for comb in combinations(range(H + W - 2), H - 1):
    h = 0
    w = 0
    seen = set([A[h][w]])
    for i in range(H + W - 2):
        if i in comb:
            h += 1
        else:
            w += 1
        seen.add(A[h][w])
    ans += len(seen) == H + W - 1

print(ans)
