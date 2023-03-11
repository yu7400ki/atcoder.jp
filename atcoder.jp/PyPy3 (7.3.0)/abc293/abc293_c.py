H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

end = (W - 1, H - 1)

def solve(pos = (0, 0), seen = set()):
    x, y = pos

    if x >= W or y >= H:
        return -1

    n = A[y][x]

    if n in seen:
        return -1

    if pos == end:
        return 0

    seen.add(n)

    ans = -1

    for dx, dy in ((1, 0), (0, 1)):
        res = solve((x + dx, y + dy), seen)

        if res != -1:
            ans += res + 1

    seen.remove(n)

    return ans

print(solve() + 1)
